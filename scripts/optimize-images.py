#!/usr/bin/env python3
"""把站点图片转成 WebP，并把 HTML 里的引用改成 .webp。

在 `nuxt generate` 之后运行：只处理 `.output/public` 产物，不动仓库里的源文件，
所以 `git pull` 不会被本地改动干扰。

  1. 对 `.output/public/images/*.png` 用 cwebp 生成同名 `.webp`（保留 alpha 通道）；
  2. 把所有 `.html` 里 `src="/images/x.png"` 改成 `.webp`（PNG 仍留在产物里，只是
     不再被引用，方便将来换 `<picture>` 做兜底）；
  3. 校验：WebP 尺寸必须与原 PNG 一致；HTML 里不应再有 `.png` 引用。

用法：python3 scripts/optimize-images.py
依赖：cwebp（Debian: apt install webp）
"""
import glob
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".output/public")
IMG_DIR = os.path.join(OUT, "images")

# 每张图的质量：扁平插画 82~85 肉眼无差别；照片可以再降到 75
QUALITY = {
    "keion-band.png": 82,
    "minori-sticker.png": 85,
}
DEFAULT_Q = 82


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError(f"不是 PNG: {path}")
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def webp_size(path):
    """不依赖 Pillow，直接从容器头读宽高（VP8 / VP8L / VP8X）。"""
    with open(path, "rb") as f:
        data = f.read(30)
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError(f"不是 WebP: {path}")
    fmt = data[12:16]
    if fmt == b"VP8 ":
        return (int.from_bytes(data[26:28], "little") & 0x3FFF,
                int.from_bytes(data[28:30], "little") & 0x3FFF)
    if fmt == b"VP8L":
        b = int.from_bytes(data[21:25], "little")
        return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
    if fmt == b"VP8X":
        return (int.from_bytes(data[24:27], "little") + 1,
                int.from_bytes(data[27:30], "little") + 1)
    raise ValueError(f"未知 WebP 子格式 {fmt!r}: {path}")


def main() -> int:
    if not os.path.isdir(IMG_DIR):
        print(f"[img] 没有目录 {IMG_DIR}，跳过", file=sys.stderr)
        return 0

    total_before = total_after = 0
    converted = []
    for png in sorted(glob.glob(os.path.join(IMG_DIR, "*.png"))):
        name = os.path.basename(png)
        webp = os.path.splitext(png)[0] + ".webp"
        q = QUALITY.get(name, DEFAULT_Q)
        subprocess.run(
            ["cwebp", "-quiet", "-q", str(q), "-alpha_q", "100", "-m", "6", "-mt",
             png, "-o", webp],
            check=True,
        )
        pw, ph = png_size(png)
        ww, wh = webp_size(webp)
        before, after = os.path.getsize(png), os.path.getsize(webp)
        total_before += before
        total_after += after
        converted.append((name, os.path.basename(webp)))
        ok = "OK" if (pw, ph) == (ww, wh) else f"尺寸不符 {pw}x{ph} vs {ww}x{wh}"
        print(f"[img] {name}: {before/1024:.0f}K -> {after/1024:.0f}K "
              f"({100*after/before:.0f}%) q={q} {ww}x{wh} {ok}")

    # 改写 HTML 引用
    replaced = 0
    for html_path in glob.glob(os.path.join(OUT, "**/*.html"), recursive=True):
        with open(html_path, encoding="utf-8") as f:
            src = f.read()
        new = src
        for png_name, webp_name in converted:
            if not os.path.exists(os.path.join(IMG_DIR, webp_name)):
                continue
            for quote in ('"', "'"):
                old_ref = f"{quote}/images/{png_name}{quote}"
                new_ref = f"{quote}/images/{webp_name}{quote}"
                replaced += new.count(old_ref)
                new = new.replace(old_ref, new_ref)
        if new != src:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(new)

    print(f"[img] 合计 {total_before/1024:.0f}K -> {total_after/1024:.0f}K，"
          f"改写引用 {replaced} 处")

    leftovers = sorted({
        os.path.basename(p)
        for p in glob.glob(os.path.join(OUT, "**/*.html"), recursive=True)
        if any(".png" in line and "/images/" in line
               for line in open(p, encoding="utf-8"))
    })
    if leftovers:
        print(f"[img] 警告：这些页面仍引用 .png: {leftovers}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""按站点实际用字裁剪显示字体（ByongGye）。

在 `nuxt generate` 之后运行：从 `.output/public` 的预渲染 HTML 里取出所有可见字符，
加上 ASCII 与常用中/日标点作为安全余量，再对 `public/fonts` 下的大字体做子集化，
写回 `.output/public/fonts/`（只改产物，不动仓库里的源字体）。

用法：python3 scripts/subset-font.py
依赖：python3-fonttools python3-brotli（Debian: apt install python3-fonttools python3-brotli）
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".output/public")

# 显示字体（大文件）。字体只用在 >=32px 的展示字上：hero 标题、navbar 品牌、
# 气泡、贴纸、大号 joining 标题等；小字一律走 --font-body 系统字体。
TARGETS = ["nano-byong-gye-hei.woff2"]

# 安全字符集：ASCII 可打印 + 常用中日标点 + 音乐/箭头符号。
# 这样改文案（用常见字符）不会缺字；真遇到生僻字会打印警告。
SAFETY = (
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "　、。，．；：？！「」『』（）《》〈〉【】〔〕—…·～〜ー♪♫→←↑↓★☆©®™°±×÷"
    + "０１２３４５６７８９"
)


def collect_chars() -> str:
    """从产物 HTML 里收集可见文本 + 安全集。"""
    text = []
    for f in glob.glob(os.path.join(OUT, "**/*.html"), recursive=True):
        with open(f, encoding="utf-8") as fh:
            html = fh.read()
        html = re.sub(r"<script.*?</script>|<style.*?</style>", "", html, flags=re.S)
        text.append(re.sub(r"<[^>]+>", "", html))  # 含属性里的 data-text
    body = re.sub(r"&[a-zA-Z]+;|&#\d+;", "", "".join(text))
    chars = set(body) - set("\n\t\r")
    chars |= set(SAFETY)
    return "".join(sorted(chars))


def main() -> int:
    if not os.path.isdir(OUT):
        print(f"找不到 {OUT}，先跑 nuxt generate", file=sys.stderr)
        return 1

    chars = collect_chars()
    cjk = sum(1 for c in chars if "\u3000" <= c <= "\u9fff")
    print(f"[subset] 需要字符 {len(chars)} 个（其中 CJK {cjk} 个）")

    from fontTools.ttLib import TTFont

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as tf:
        tf.write(chars)
        text_file = tf.name
    try:
        for name in TARGETS:
            src = os.path.join(ROOT, "public/fonts", name)
            dst = os.path.join(OUT, "fonts", name)
            if not os.path.exists(src):
                print(f"[subset] 跳过（源文件不存在）: {name}")
                continue
            before = os.path.getsize(src)
            subprocess.run(
                [
                    sys.executable, "-m", "fontTools.subset", src,
                    f"--text-file={text_file}",
                    "--flavor=woff2",
                    "--layout-features=*",
                    f"--output-file={dst}",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            cmap = set(TTFont(dst).getBestCmap())
            missing = [c for c in chars if ord(c) not in cmap]
            after = os.path.getsize(dst)
            print(
                f"[subset] {name}: {before/1024:.0f}K -> {after/1024:.0f}K "
                f"({100*after/before:.1f}%) 缺字 {len(missing)}"
            )
            if missing:
                print(f"[subset] 警告：缺字 {''.join(missing)}", file=sys.stderr)
    finally:
        os.unlink(text_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

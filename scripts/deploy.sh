#!/usr/bin/env bash
# 构建 + 优化 + 发布到静态根目录（默认站点 k-on.zznfzx.com）
#
#   ./scripts/deploy.sh                  # 用默认 DEST
#   DEST=/var/www/xxx ./scripts/deploy.sh
#
# 要求：node >= 20（Debian 用 apt 的 nodejs，别用 pi/nvm 的私有运行时目录，
# 否则升级 node 后 cron/脚本会静默失效）、cwebp、python3-fonttools、python3-brotli。
#   apt install nodejs npm webp python3-fonttools python3-brotli
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${DEST:-/var/www/k-on.zznfzx.com}"
SITE="${SITE:-https://k-on.zznfzx.com/}"

cd "$ROOT"

[ -d node_modules ] || npm ci --omit=dev --no-audit --no-fund
# 内存小（1.9G）的机器限一下堆，否则 nitro 偶发 OOM
NODE_OPTIONS="${NODE_OPTIONS:---max-old-space-size=1024}" npm run generate

# 产物体积优化：字体按实际用字裁剪、图片转 WebP（都只改 .output，不动源文件）
python3 scripts/subset-font.py
python3 scripts/optimize-images.py

rsync -a --delete "$ROOT/.output/public/" "$DEST"/
chown -R root:root "$DEST" 2>/dev/null || true

# 冒烟：页面与关键资源都要 200
code=$(curl -s -o /dev/null -w '%{http_code}' "$SITE")
echo "deployed $(git rev-parse --short HEAD) -> $SITE ($code)"
[ "$code" = "200" ] || { echo "冒烟失败" >&2; exit 1; }

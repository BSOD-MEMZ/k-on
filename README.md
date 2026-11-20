# 軽音部 · 超魔丸バスターズ

株洲南方中学轻音部招新官网。Nuxt 4 + 手写 CSS，风格照着社团宣传海报来：奶油纸底、轻音绿、半调点阵、粗圆标题字、贴纸和气泡。

## 跑起来

```bash
npm install
npm run dev      # http://localhost:3000
npm run build    # 生产构建
npm run generate # 纯静态导出到 .output/public
```

## 结构

```
app/
  app.vue                    # <NuxtPage />
  pages/index.vue            # 整站单页（hero / 关于 / 招新 / 联系 / footer）
  assets/css/main.css        # 全部样式与设计变量
public/
  fonts/nano-byong-gye-hei.woff2   # 海报同款标题字（从 ITExWeb 复制）
  images/keion-band.png            # hero 立绘（白底已抠成透明，来自群友给的原图）
  favicon.svg
```

## 改内容改哪里

- 文案、乐器位、招新步骤、QQ 号：`app/pages/index.vue` 里的 `tickerItems` / `slots` / `steps` 和模板。
- 配色、圆角、点阵、字重：`app/assets/css/main.css` 顶部 `:root` 变量，主色是 `--g-400: #96c545`。
- 标题字 `ByongGye` 是超粗展示字，**只在 ≥32px 的大字上用**；小字（按钮 / 卡片标题 / navbar 品牌 / tab）一律走 `--font-body`，否则中文会糊成块。这是这套字库的坑，别踩。
  hero 大标题 `軽音部` 用的就是这个字体（≈152px），navbar 品牌下行 34px 也是它。
- 入场动画用 CSS `animation-timeline: view()`，不依赖 JS，浏览器不支持时内容直接可见。

## 已知取舍

- 没有后端。QQ 号码是复制按钮，不做提交接口。
- 站点是单页，锚点跳转（`#about` `#slots` `#join` `#contact`）。

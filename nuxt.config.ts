export default defineNuxtConfig({
  compatibilityDate: '2025-01-01',
  devtools: { enabled: false },
  css: ['~/assets/css/main.css'],
  app: {
    head: {
      htmlAttrs: { lang: 'zh-CN' },
      title: '軽音部 超魔丸バスターズ · 南方中学軽音部 立部决定！',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            '株洲南方中学轻音部（超魔丸バスターズ）官方网站。无论你是谁，只要热爱音乐，这里就是你的舞台。周三第九节课，体育馆，不见不散！'
        },
        { name: 'theme-color', content: '#96c545' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'preload', as: 'font', type: 'font/woff2', href: '/fonts/nano-byong-gye-hei.woff2', crossorigin: '' }
      ]
    }
  }
})

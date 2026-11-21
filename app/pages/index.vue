<template>
  <div class="page">
    <!-- ================= 施工横幅 ================= -->
    <div class="banner">
      <div class="banner-inner">
        <img class="banner-mascot" src="/images/minori-sticker.png" alt="施工中" width="296" height="256" />
        本站正在施工中，部分内容与信息随时可能调整
        <span class="banner-en">Work in progress</span>
      </div>
    </div>

    <!-- ================= NAV ================= -->
    <header class="nav">
      <div class="wrap nav-inner">
        <a class="brand" href="#top">
          <span class="brand-main">軽音部</span>
          <span class="brand-sub">超魔丸バスターズ</span>
        </a>
        <nav class="nav-links">
          <a href="#about">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            关于我们
          </a>
          <a href="#slots">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>
            在找谁
          </a>
          <a href="#join">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>
            招新信息
          </a>
          <a href="#contact">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
            联系部长
          </a>
        </nav>
      </div>
    </header>

    <main id="top">
      <!-- ================= HERO ================= -->
      <section class="hero">
        <div class="hero-corner" />
        <div class="dots" style="left: -120px; top: 180px; width: 380px; height: 380px" />
        <div class="dots" style="right: 42%; bottom: -60px; width: 300px; height: 300px; opacity: 0.6" />

        <div class="wrap hero-grid">
          <div>
            <div class="kicker">株洲南方中学 · 軽音部</div>

            <h1 class="hero-title">軽音部</h1>

            <div class="hero-line">
              <span class="bubble display" style="font-size: clamp(20px, 2.6vw, 30px)">立部决定！</span>
              <span class="display outlined hero-echo" data-text="けいおん!!!">けいおん!!!</span>
            </div>

            <p class="hero-lead">
              来组一辈子乐队吧？<b>一緒に！</b>
              如果你平时喜欢听歌，偶尔想唱歌、想玩乐器，却一直找不到伙伴——那就看看这里。
              无论你是谁，只要热爱音乐，南方中学就是你的舞台。
              没有严苛的门槛，只要你愿意花时间，<b>那颗炽热的心就是最好的入场券</b>。
            </p>

            <div class="hero-actions">
              <a class="btn" href="#join">立即报名 →</a>
              <a class="btn ghost" href="#about">我们是谁？</a>
            </div>
          </div>

          <div class="hero-art">
            <img class="band-art" src="/images/keion-band.png" alt="軽音部成员立绘" width="1054" height="1492" />
            <div class="hero-sticker s1">♪ けいおん!!</div>
            <div class="hero-sticker s2">部員募集中 ♪</div>
            <!-- doodles -->
            <svg class="doodle floaty" style="left: 0; bottom: 4%; --rot: -12deg" width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 18V6l9-2v12" />
              <circle cx="6.6" cy="18" r="2.4" />
              <circle cx="15.6" cy="16" r="2.4" />
            </svg>
            <svg class="doodle floaty" style="right: 6%; top: 2%; --rot: 14deg; animation-delay: -2s" width="34" height="34" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2.5l2.4 6.1 6.1 2.4-6.1 2.4L12 19.5l-2.4-6.1L3.5 11l6.1-2.4z" />
            </svg>
          </div>
        </div>
      </section>

      <!-- ================= TICKER ================= -->
      <div class="ticker">
        <div class="ticker-track">
          <div v-for="g in 4" :key="g" style="display: flex">
            <span v-for="(t, i) in tickerItems" :key="g + '-' + i">
              {{ t }} <i>♪</i>
            </span>
          </div>
        </div>
      </div>

      <!-- ================= ABOUT ================= -->
      <section id="about" class="section">
        <div class="dots" style="right: -140px; top: 40px; width: 420px; height: 420px; opacity: 0.5" />
        <div class="wrap">
          <div class="section-head reveal">
            <h2 class="display">我们是<br />軽音部</h2>
            <span class="en">僕らは軽音部！！！</span>
          </div>

          <div class="cards">
            <article class="card reveal">
              <span class="no">01</span>
              <h3>全新社团</h3>
              <p>
                这是个新成立的社团，追求新的音乐风格，涵盖 J-POP，术力口等等！
                资历不深但信心不小！
              </p>
              <span class="tag">prenew</span>
            </article>
            <article class="card reveal">
              <span class="no">02</span>
              <h3>器材社团共享</h3>
              <p>
                键盘、电吉他、贝斯、鼓组都在社团。手里没琴也能先来玩，
                先喜欢上，再谈买不买。
              </p>
              <span class="tag">Gear for all</span>
            </article>
            <article class="card reveal">
              <span class="no">03</span>
              <h3>一起站上舞台</h3>
              <p>
                校园艺术节、社团文化节、校外的 Livehouse。
                练到能演出的那天，灯光、回声和尖叫都属于我们。
              </p>
              <span class="tag">On stage</span>
            </article>
          </div>
        </div>
      </section>

      <!-- ================= SLOTS ================= -->
      <section id="slots" class="section band">
        <svg class="doodle floaty" style="left: 3%; top: 34px; --rot: -8deg" width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <circle cx="7" cy="8" r="2.1" /><circle cx="13" cy="6" r="2.1" /><circle cx="17" cy="10" r="2.1" />
          <path d="M12 11c-3.6 0-6.4 2.4-6.4 5.4 0 1.6 1.2 2.6 2.8 2.6 1.3 0 2.3-.7 3.6-.7s2.3.7 3.6.7c1.6 0 2.8-1 2.8-2.6C18.4 13.4 15.6 11 12 11z" />
        </svg>
        <div class="wrap">
          <div class="section-head reveal">
            <h2 class="display">正在找人</h2>
            <span class="en">Open slots</span>
          </div>

          <div class="slots">
            <div v-for="s in slots" :key="s.name" class="slot reveal">
              <span v-if="s.hot" class="hot">需要</span>
              <div class="ico">{{ s.en }}</div>
              <h4>{{ s.name }}</h4>
              <p>{{ s.desc }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- ================= JOIN ================= -->
      <section id="join" class="section">
        <div class="wrap">
          <div class="join reveal">
            <div class="sub">Offline recruitment</div>
            <h2 class="display">线下招新</h2>
            <dl class="join-grid">
              <div class="jcell">
                <dt>时间 / When</dt>
                <dd>周三 第九节课</dd>
              </div>
              <div class="jcell">
                <dt>地点 / Where</dt>
                <dd>体育馆</dd>
              </div>
              <div class="jcell">
                <dt>带什么 / Bring</dt>
                <dd>你自己就好</dd>
              </div>
            </dl>
            <p class="note">
              不用准备曲目，不用背自我介绍。人来就行——想唱两句、想摸一下琴，都可以现场来。
              实在来不了，直接加群或者敲部长，一样算报名。
            </p>
          </div>

          <div class="steps">
            <div v-for="s in steps" :key="s.t" class="step reveal">
              <b>{{ s.t }}</b>{{ s.d }}
            </div>
          </div>
        </div>
      </section>

      <!-- ================= CONTACT ================= -->
      <section id="contact" class="section tight">
        <div class="dots" style="left: -100px; bottom: 20px; width: 340px; height: 340px; opacity: 0.5" />
        <div class="wrap">
          <div class="section-head reveal">
            <h2 class="display">联系方式</h2>
            <span class="en">Say hi</span>
            <p>别害羞，QQ 直接加，备注写「轻音部招新」就行。</p>
          </div>

          <div class="contact-grid">
            <div class="idcard reveal">
              <div class="role">部长 / President</div>
              <div class="who">姜文凯</div>
              <p style="margin: 6px 0 0; font-size: 13px; color: var(--ink-soft)">2517 班</p>

              <div class="copy-row">
                <div>
                  <span>部长 QQ</span>
                  <div><strong>737519785</strong></div>
                </div>
                <button class="mini" :class="{ done: copied === '737519785' }" @click="copy('737519785')">
                  {{ copied === '737519785' ? '已复制' : '复制' }}
                </button>
              </div>
              <div class="copy-row">
                <div>
                  <span>軽音部 QQ 群</span>
                  <div><strong>1134805109</strong></div>
                </div>
                <button class="mini" :class="{ done: copied === '1134805109' }" @click="copy('1134805109')">
                  {{ copied === '1134805109' ? '已复制' : '复制' }}
                </button>
              </div>
            </div>

            <div class="quote reveal">
              <p>
                <span class="q-lead">没有严苛的门槛</span>
                只要你愿意花时间，那颗炽热的心，<br />便是最好的证明。
              </p>
              <small>— 軽音部 · 超魔丸バスターズ</small>
            </div>

            <div class="idcard reveal dlcard">
              <div class="role">Join us</div>
              <div class="who" style="font-size: 23px; line-height: 1.4">入部报名表</div>
              <p class="dl-note">
                可以打印后手写填好交给部长，也可以直接填在电子稿上发给社长
              </p>
              <a class="btn" href="/files/entry-form.docx" download="轻音部入部报名表.docx">
                下载报名表 <span class="dl-meta">DOCX · 50 KB</span>
              </a>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- ================= FOOTER ================= -->
    <footer class="footer">
      <div class="wrap">
        <div class="bigjoin display">
          <div class="row"><span class="solid">JOIN</span><span class="block">US</span></div>
          <div class="row"><span class="ghost">NOW</span><span class="solid" style="font-size: 0.55em">けいおん!!!</span></div>
        </div>
        <div class="foot-meta">
          <span>© 2026 株洲南方中学 軽音部 · 超魔丸バスターズ</span>
          <span>周三第九节课 · 体育馆 · 不见不散！</span>
          <span>Made with ♪ by 軽音部</span>
        </div>
      </div>
    </footer>

    <div class="toast" :class="{ show: toast }">{{ toast }}</div>
  </div>
</template>

<script setup>
useHead({
  title: '軽音部 超魔丸バスターズ · 南方中学軽音部 立部决定！'
})

const tickerItems = [
  '线下招新',
  '周三第九节课',
  '体育馆',
  '零基础欢迎',
  'けいおん!!!',
  '一起来组一辈子乐队吧'
]

const slots = [
  { name: '主唱', en: 'VOCAL', desc: '初音未来', hot: true },
  { name: '吉他', en: 'GUITAR', desc: '节奏 / 主音都行', hot: false },
  { name: '贝斯', en: 'BASS', desc: 'buzzz…', hot: false },
  { name: '键盘', en: 'KEYBOARD', desc: '社团有琴', hot: false },
  { name: '鼓', en: 'DRUMS', desc: '慢一点也没关系', hot: false }
]

const steps = [
  { t: '找到我们', d: '周三第九节课，体育馆门口绿色海报旁。' },
  { t: '留个 QQ', d: '找部长姜文凯签到，方便之后通知。' },
  { t: '随便玩两下', d: '唱两句、弹一段、或者只是坐着听。' },
  { t: '加群等排练', d: '1134805109，排练时间群里通知。' }
]

const copied = ref('')
const toast = ref('')
let timer

async function copy (text) {
  try {
    await navigator.clipboard.writeText(text)
  } catch {
    const el = document.createElement('textarea')
    el.value = text
    document.body.appendChild(el)
    el.select()
    document.execCommand('copy')
    el.remove()
  }
  copied.value = text
  toast.value = '已复制 ' + text
  clearTimeout(timer)
  timer = setTimeout(() => {
    copied.value = ''
    toast.value = ''
  }, 1800)
}

// 入场动画走 CSS scroll-driven animation，无 JS 依赖，首屏永远可读

</script>

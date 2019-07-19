import Vue from 'vue'
import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css

import App from './App'
import router from './router'
import store from './store'

import '@/icons' // icon
import '@/permission' // permission control

Vue.use(ElementUI, { locale })

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
import hljs from 'highlight.js'
import 'highlight.js/styles/monokai.css'

Vue.directive('highlight', function(el) {
  const blocks = el.querySelectorAll('pre code')
  setTimeout(() => {
    blocks.forEach((block) => {
      hljs.highlightBlock(block)
    })
  }, 200)
})

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/css/main.css'
import BlogApp from './BlogApp'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
Vue.config.productionTip = false
/* eslint-disable no-new */
Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  router,
  template: '<BlogApp/>',
  components: {
    BlogApp
  }
})

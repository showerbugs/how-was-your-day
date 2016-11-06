import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './vuex/store'

const app = new Vue({
  router,
  store,
  ...App
})
app.$mount('#app')
export { app, router, store }

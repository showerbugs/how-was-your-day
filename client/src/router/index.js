import Vue from 'vue'
import Daily from '../components/Daily.vue'
import Organization from '../components/Organization.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/daily', component: Daily },
    { path: '/organization', component: Organization }
  ]
})

export default router

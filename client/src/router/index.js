import Vue from 'vue'
import Team from '../components/TeamView.vue'
import Organization from '../components/Organization.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/team', component: Team },
    { path: '/organization', component: Organization }
  ]
})

export default router

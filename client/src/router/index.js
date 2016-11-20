import Vue from 'vue'
import Project from '../components/Project.vue'
import Organization from '../components/Organization.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/project', component: Project },
    { path: '/organization', component: Organization }
  ]
})

export default router

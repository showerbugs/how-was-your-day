import Vue from 'vue'
import Signin from '../components/Signin.vue'
import Signup from '../components/Signup.vue'
import Team from '../components/TeamView.vue'
import Organization from '../components/Organization.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', component: Signin},
    {path: '/Signin', component: Signin},
    {path: '/signup', component: Signup},
    {path: '/team/:teamId', name: 'team', component: Team },
    {path: '/organization', component: Organization }
  ]
})

export default router

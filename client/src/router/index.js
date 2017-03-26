import Vue from 'vue'
import Signin from '../components/Signin.vue'
import Signup from '../components/Signup.vue'
import Team from '../components/TeamView.vue'
import CreateTeam from '../components/CreateTeam.vue'
import Organization from '../components/Organization.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', component: Signin},
    {path: '/signin', component: Signin},
    {path: '/signup', component: Signup},
    {path: '/team/new', component: CreateTeam},
    {path: '/team/:teamId', name: 'team', component: Team },
    {path: '/organization', component: Organization }
  ]
})
// router.beforeEach((to, from, next) => {
//   console.log(to, from, next)
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     // 이 라우트는 인증이 필요하며 로그인 한 경우 확인하십시오.
//     // 그렇지 않은 경우 로그인 페이지로 리디렉션하십시오.
//     if (!auth.loggedIn()) {
//       next({
//         path: '/signin',
//         query: { redirect: to.fullPath }
//       })
//     } else {
//       next()
//     }
//   } else {
//     next() // 반드시 next()를 호출하십시오!
//   }
// })
export default router

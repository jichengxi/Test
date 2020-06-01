import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './router'

Vue.use(VueRouter)

const router = new VueRouter({
  // mode: 'history',
  routes: routes
})

// 前置守卫
const HAS_LOGIN = true
// to：去的页面 from：当前离开的页面 next：执行的函数
router.beforeEach((to, from, next) => {
  if (to.name !== 'login') {
    if (HAS_LOGIN) next()
    else next({ name: 'login' })
  } else {
    if (HAS_LOGIN) next({ name: 'Home' })
    else next()
  }
})

// 导航被确认前，异步路由组件被解析之后触发
// router.beforeResolve((to, from, next) => {
//   //
// })

// 后置守卫
// router.afterEach((to, from) => {
//   // logining = false
// })

export default router

// 1. 导航被触发
// 2. 在失活的组件(即将离开的页面组件)里调用离开守卫 beforeRouteLeave
// 3. 调用全局的前置守卫 beforeEach
// 4. 在重用的组件里调用 beforeRouteUpdate
// 5. 调用路由独享的守卫 beforEnter
// 6. 解析异步路由组件
// 7. 在被激活的组件(即将进入的页面组件)里调用 beforeRouteEnter
// 8. 调用全局的解析守卫 beforeResolve
// 9. 导航被确认
// 10. 调用全局的后置守卫 afterEach
// 11. 触发DOM更新
// 12. 用创建好的实例调用beforeRouterEnter守卫里传给next的回调函数

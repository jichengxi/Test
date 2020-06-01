import Home from '@/views/Home.vue'

export default [
  {
    path: '/',
    name: 'Home',
    alias: '/home_page',
    component: Home,
    props: route => ({
      food: route.query.food
    }),
    // 路由独享守卫
    beforeEnter: (to, from, next) => {
      // if (from.name === 'About') alert('这是从About页来的')
      // else alert('这不是从About页来的')
      // console.log(from.name)
      next()
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue'),
    props: {
      food: 'banana'
    }
  },
  {
    path: '/argu/:name',
    name: 'argu',
    component: () => import('@/views/argu.vue'),
    props: true
  },
  {
    path: '/parent',
    name: 'parent',
    component: () => import('@/views/parent.vue'),
    children: [
      {
        path: 'child',
        component: () => import('@/views/child.vue')
      }
    ]
  },
  {
    path: '/named_view',
    components: {
      default: () => import('@/views/child.vue'),
      email: () => import('@/views/email.vue'),
      tel: () => import('@/views/tel.vue')
    }
  },
  {
    path: '/main',
    // redirect: '/'
    // redirect: {
    //   name: 'Home'
    // }
    redirect: to => {
      // console.log(to)
      return {
        name: 'Home'
      }
    }
  },
  {
    path: '*',
    component: () => import('@/views/error_404.vue')
  }
]

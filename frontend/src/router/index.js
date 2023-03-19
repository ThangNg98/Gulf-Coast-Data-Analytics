import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      props: true,
      component: () => import('../views/Home.vue')
    },
    {
      path: '/register',
      name: 'Register',
      props: true,
      component: () => import('../views/Register.vue')
    },
    {
      path: '/profile',
      name: 'Profile',
      props: true,
      component: () => import('../views/Profile.vue'),
      children: [
        {
          path: '/checkin',
          component: () => import('@/components/CheckIn.vue')
        },
        {
          path: '/history',
          component: () => import('@/components/History.vue')
        },
        {
          path: '/update',
          component: () => import('@/components/UpdateProfile.vue')
        }
      ]
    },
  ]
})

export default router

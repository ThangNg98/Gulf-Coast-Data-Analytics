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
      name: 'Profile',
      props: true,
      component: () => import('../views/Profile.vue'),
      children: [
        {
          path: '/profile/checkin',
          component: () => import('@/components/V_CheckIn.vue')
        },
        {
          path: '/profile/history',
          component: () => import('@/components/V_History.vue')
        },
        {
          path: '/profile/update',
          component: () => import('@/components/V_UpdateProfile.vue')
        }
      ]
    },
  ]
})

export default router

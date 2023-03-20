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
      path: '/volunteers',
      name: 'Volunteers',
      props: true,
      component: () => import('../components/Volunteers.vue')
    },
    {
      path: '/update_volunteer',
      name: 'VolunteersUpdate',
      props: true,
      component: () => import('../components/VolunteersUpdate.vue')
    },
  ]
})

export default router

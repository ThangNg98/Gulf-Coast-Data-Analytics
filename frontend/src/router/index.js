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
      path: '/events',
      name: 'Events',
      props: true,
      component: () => import('../components/Events.vue')
    },
    {
      path: '/update_event',
      name: 'EventsUpdate',
      props: true,
      component: () => import('../components/EventsUpdate.vue')
    },
    {
      path: '/create_event',
      name: 'EventsCreate',
      props: true,
      component: () => import('../components/EventsCreate.vue')
    },
  ]
})

export default router

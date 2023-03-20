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
      path: '/admindash',
      name: 'Admin Dashboard',
      props: true,
      component: () => import('../views/AdminDash.vue')
    },
    {
      path: '/orgs',
      name: 'Orgs',
      props: true,
      component: () => import('../components/Orgs.vue')
    },
    {
      path: '/create_org',
      name: 'OrgsCreate',
      props: true,
      component: () => import('../components/OrgsCreate.vue')
    },
    {
      path: '/update_org',
      name: 'OrgsUpdate',
      props: true,
      component: () => import('../components/OrgsUpdate.vue')
    },
  ]
})

export default router

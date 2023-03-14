import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      props: true,
      component: () => import('../components/Home.vue')
    },
    {
      path: '/register',
      name: 'Register',
      props: true,
      component: () => import('../components/Register.vue')
    },
    {
      path: '/employeelogin',
      name: 'EmployeeLogin',
      component: () => import('../Views/EmployeeLogin.vue')
    }
  ]
})

export default router

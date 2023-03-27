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
      path: '/profile',

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
    {
      name: 'Admin Dashboard',
      path: '/admin',
      props: true,
      component: () => import('../views/AdminDash.vue'),
      children: [
        {
          path: '/admin/dash',
          name: 'Admin Dashboard View',
          props: true,
          component: () => import('../components/AdminDashView.vue')
        },
        {
          path: '/admin/orgs',
          name: 'Orgs',
          props: true,
          component: () => import('../components/Orgs.vue')
        },
        {
          path: '/admin/create_org',
          name: 'OrgsCreate',
          props: true,
          component: () => import('../components/OrgsCreate.vue')
        },
        {
          path: '/admin/update_org',
          name: 'OrgsUpdate',
          props: true,
          component: () => import('../components/OrgsUpdate.vue')
        },
        {
          path: '/admin/volunteers',
          name: 'Volunteers',
          props: true,
          component: () => import('../components/Volunteers.vue')
        },
        {
          path: '/admin/update_volunteer',
          name: 'VolunteersUpdate',
          props: true,
          component: () => import('../components/VolunteersUpdate.vue')
        },
        {
          path: '/admin/events',
          name: 'Events',
          props: true,
          component: () => import('../components/Events.vue')
        },
        {
          path: '/admin/update_event',
          name: 'EventsUpdate',
          props: true,
          component: () => import('../components/EventsUpdate.vue')
        },
        {
          path: '/admin/create_event',
          name: 'EventsCreate',
          props: true,
          component: () => import('../components/EventsCreate.vue')
        },
        {
          path: '/admin/sessions_list',
          name: 'SessionsList',
          props: true,
          component: () => import('../components/SessionsList.vue')
        },
        {
          path: '/admin/update_sessions',
          name: 'SessionsUpdate',
          props: true,
          component: () => import('../components/SessionsUpdate.vue')
        }
      ]}
    ]
})

export default router

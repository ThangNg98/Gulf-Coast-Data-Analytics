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
      path: '/admindash',
      name: 'Admin Dashboard',
      props: true,
      component: () => import('../views/AdminDash.vue'),
      children: [
        {
          path: '/admindashview',
          name: 'Admin Dashboard View',
          props: true,
          component: () => import('../components/AdminDashView.vue')
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
        }
      ]}
    ]
})

export default router

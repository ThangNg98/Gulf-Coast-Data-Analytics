<!--'/admindash'-->
<template>
    <main class="">
        <div class="d-inline-block text-start ms-3">
          <nav id="contentNav" class="navbar navbar-expand-lg navbar-light navbar-brand" style="margin-top:1rem; margin-bottom:1rem">
            <button
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#contentNavbar"
              class="navbar-toggler"
              aria-controls="contentNavbar"
              aria-expanded="false"
              aria-label="Toggle navigation" style="margin-top:1rem;">
              
              <span class="navbar-toggler-icon"></span> Menu
            </button>
            <div class="collapse navbar-collapse" id="contentNavbar">
              <ul class="navbar-nav ms-auto mb-2 mb-lg-0 flex-wrap">
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/dash">Dashboard</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/reports">Reports</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/events">Events</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/orgs">Organizations</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/volunteers">Volunteers</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link text-primary" to="/admin/sessions_list">Sessions</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" to="/adminlogin" @click="handleLogout">Logout</router-link>
                </li>
              </ul>
          </div>
        </nav>
      </div>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>
<style>
    #contentNavbar .nav-link.router-link-exact-active{
        background-color: #eee;
    }
    /* Medium Devices, Desktops */
    @media only screen and (min-width : 992px) {
        main {
            text-align: center;
        }
        #contentNavbar .nav-item {
            border: 1px solid black;
            border-right: none;
        }
        #contentNavbar .nav-item:last-child {
            border: 1px solid black;
        }
    }
</style>

<script>
import AdminDashView from "@/components/AdminDashView.vue"
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

    export default {
        name: 'Admin Dashboard',
        components: {
            AdminDashView,
        },
        methods: {
            handleLogout() {
                useAdminLoginStore().logout()
            }
        }
    }
</script>
<!--'/admindash'-->
<template>
    <main class="text-center">
        <div>
            <nav class="nav justify-content-center mb-3" style="margin-top: 2rem; margin-bottom: 2rem">
                <router-link class="nav-link" to="/admindashview">Dashboard</router-link>
                <router-link class="nav-link" to="/events">Events</router-link>
                <router-link class="nav-link" to="/orgs">Organizations</router-link>
                <router-link class="nav-link" to="/volunteers">Volunteers</router-link>
                <router-link class="nav-link" to="/sessions_list">Sessions</router-link>
                <router-link class="nav-link" to="/adminlogin" @click="handleLogout">Logout</router-link>
            </nav>
        </div>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>
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
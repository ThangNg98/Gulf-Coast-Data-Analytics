<!--'/admindash'-->
<template>
    <main class="text-center">
        <div class="d-inline-block">
            <nav class="in-page-nav-bar nav  border border-dark justify-content-center" style="margin-top: 2rem;">
                <router-link class="nav-link border-end border-dark" to="/admin/dash">Dashboard</router-link>
                <router-link class="nav-link border-end border-dark" to="/admin/events">Events</router-link>
                <router-link class="nav-link border-end border-dark" to="/admin/orgs">Organizations</router-link>
                <router-link class="nav-link border-end border-dark" to="/admin/volunteers">Volunteers</router-link>
                <a class="nav-link">Sessions</a>
            </nav>
        </div>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>
<style>
    .in-page-nav-bar .nav-link.router-link-exact-active{
        background-color: #eee;
    }
</style>
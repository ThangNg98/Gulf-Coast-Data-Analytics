<template>
    <main>
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Profile</h1> <!--header-->
            <div class="d-inline-block mb-5">
                <nav class="in-page-nav-bar nav border border-dark">
                    <router-link class="nav-link border-end border-dark p-2" to="/profile/checkin">Check In/Out</router-link>
                    <router-link class="nav-link border-end border-dark p-2" to="/profile/history">History</router-link>
                    <router-link class="nav-link p-2" to="/profile/update">Update Profile</router-link>
                </nav>
            </div>
        </div>

        <div>
            <router-view></router-view>
        </div>
    </main>
</template>
<script>
    export default {
        data() {
            return {
                
            }
        },
    }
</script>
<style>
    .in-page-nav-bar .nav-link.router-link-exact-active{
        background-color: #eee;
    }
</style>
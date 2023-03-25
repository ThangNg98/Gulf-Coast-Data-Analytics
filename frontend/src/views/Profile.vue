<template>
    <main>
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Profile</h1> <!--header-->
            <div class="d-inline-block mb-5">
                <nav class="nav border border-dark">
                    <router-link class="nav-link border-end border-dark" to="/profile/checkin">Check In</router-link>
                    <router-link class="nav-link border-end border-dark" to="/profile/history">History</router-link>
                    <router-link class="nav-link" to="/profile/update">Update Profile</router-link>
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
    .nav-link.router-link-exact-active{
        background-color: #eee;
    }
</style>
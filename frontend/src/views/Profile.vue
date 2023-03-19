<template>
    <main class="text-center w-100">
        <h1 style="margin-top: 2rem; margin-bottom: 2rem">Profile</h1> <!--header-->
        <div class="d-inline-block mb-5">
            <nav class="nav">
                <router-link class="nav-link active" aria-current="page" to="/checkin">CheckIn</router-link>
                <router-link class="nav-link" to="/history">History</router-link>
                    <router-link class="nav-link" to="/update">Update Profile</router-link>
            </nav>
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
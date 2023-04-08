<template>
    <main>
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem"> Welcome, {{ this.first_name }}!</h1> <!--header-->
            
            <div class="d-inline-block mb-5">
                <nav class="in-page-nav-bar nav border border-dark">
                    <router-link class="nav-link border-end border-dark p-2" to="/profile/checkin">Check In/Out</router-link>
                    <router-link class="nav-link border-end border-dark p-2" to="/profile/history">History</router-link>
                    <router-link class="nav-link border-end border-dark p-2" to="/profile/update">Update Profile</router-link>
                    <router-link class="nav-link p-2" @click="logout" to="/">Logout</router-link>
                </nav>
            </div>
            
        </div>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>
<script>
import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore.js'
import axios from 'axios';

    export default {
        data() {
            return {
                first_name: useVolunteerPhoneStore().volunteer_first_name
            }
        },
        mounted() {
           //this.getVolunteerName()

        },
        methods: {
            async getVolunteerName() {
                const phone = useVolunteerPhoneStore().volunteerPhone
                axios
                    .get(`http://127.0.0.1:5000/get_volunteer_id/${phone}`)
                    .then((response) => {
                        this.first_name = response.data[0].first_name
                        console.log(this.first_name)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            logout() {
                console.log('logout called')
                useVolunteerPhoneStore().clearVolunteerPhone()
            }

        }
    }
</script>
<style>
    .in-page-nav-bar .nav-link.router-link-exact-active{
        background-color: #eee;
    }
</style>
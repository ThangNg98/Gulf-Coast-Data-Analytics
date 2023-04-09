<template>
    <main>
        <div class="text-center">
            <h1 style="margin-top: 2rem;"> Welcome, {{ this.first_name }}!</h1> <!--header-->
            
            <div class="d-inline-block text-start w-100">
                <nav id="contentNav" class="navbar navbar-expand-lg navbar-light navbar-brand w-75 ms-auto me-auto" style="margin-bottom:1rem; min-width: 300px;">
                    <button
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#contentNavbar"
                    class="navbar-toggler mb-1"
                    style="z-index: 5;"
                    aria-controls="contentNavbar"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span> Menu
                    </button>
                    <div class="collapse navbar-collapse" id="contentNavbar">
                        <ul class="navbar-nav ms-auto me-auto mb-2 mb-lg-0 flex-wrap">
                            <li class="nav-item">
                                <router-link class="nav-link text-primary" to="/profile/checkin">Check In/Out</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link text-primary" to="/profile/history">History</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link text-primary" to="/profile/update">Update Profile</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" @click="logout" to="/">Logout</router-link>
                            </li>
                        </ul>
                    </div>
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
            console.log('useVolunteerPhoneStore', useVolunteerPhoneStore().volunteer_first_name)
            this.first_name = useVolunteerPhoneStore().volunteer_first_name
        },
        methods: {
            logout() {
                console.log('logout called')
                useVolunteerPhoneStore().clearVolunteerPhone()
            }
        }
    }
</script>
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
<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: left; max-width: 50%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Volunteer Name</th>
                        <th scope="col">Session Date</th>
                        <th scope="col">Event</th>
                        <th scope="col">Organization</th>
                        <th scope="col">Start Time</th>
                        <th scope="col">Finish Time</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr >
                            <td> <router-link class="nav-link" to="/admin/update_sessions"> John Smith </router-link></td>
                            <td> 3/5/2023 </td>
                            <td> Garden </td>
                            <td> UH Garden Team </td>
                            <td> 2:00 PM </td>
                            <td> null </td>
                        </tr>
                        <tr>
                            <td> <router-link class="nav-link" to="/admin/update_sessions"> Jane Doe </router-link></td>
                            <td> 3/5/2023 </td>
                            <td> Garden </td>
                            <td> UH Garden Team </td>
                            <td> 2:00 PM </td>
                            <td> null </td>
                        </tr>

                    </tbody>
                </table>
        </div>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'SessionsList',
    data() {
        return {
            msg : "Active Sessions List",
        };

    },
    methods: {
        submitForm() {
        }


    }
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto

}

.table td {
    word-wrap: break-word;
    min-width: 160px;
    max-width: 160px;
}
</style>
<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 50%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Event Name</th>
                        <th scope="col">Description</th>
                        </tr>
                    </thead>
                    <tbody>   
                        <tr>
                            <td> <router-link class="nav-link" to="/admin/update_event"> Garden </router-link></td>
                            <td> <router-link class="nav-link" to="/admin/update_event"> Garden at the Living Legacy Center </router-link></td>
                        </tr>
                        <tr>
                            <td>Market</td>
                            <td>Market at the Living Legacy Center</td>
                        </tr>

                    </tbody>
                </table>
        </div>
        <div style="text-align:right; margin-top: 2rem;">
            <router-link class="nav-link" to="/admin/create_event"> <button type="submit" class="btn btn-success" style="margin-right:0.5rem" >Create New Event</button> </router-link>
        </div>

    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'Events',
    data() {
        return {
            msg : "List of Events",
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
    min-width: 120px;
    max-width: 160px;
}
</style>
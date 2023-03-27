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
                        <th scope="col">Volunteer Name</th>
                        <th scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td> <router-link class="nav-link" to="/admin/update_volunteer"> John Smith </router-link></td>
                            <td> <router-link class="nav-link" to="/admin/update_volunteer"> 53 </router-link></td>
                        </tr>
                        <tr>
                            <td>Jane Doe</td>
                            <td>21</td>
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
    name: 'Volunteers',
    data() {
        return {
            msg : "List of Volunteers",
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
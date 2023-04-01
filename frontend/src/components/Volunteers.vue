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
                        <th scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="volunteer in volunteers"
                        @click="editVolunteers(volunteer.volunteer_id)">
                            <td>{{ volunteer.first_name }} {{ volunteer.last_name }}</td>
                            <td>{{ volunteer.total_hours }}</td>
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
            volunteers: [],
        };

    },
    methods: {
        getVolunteers() {
            axios.get('http://127.0.0.1:5000/read_volunteers')
            .then(response => {
                // iterate through JSON response and add volunteers to the volunteer array
                for (var i = 0; i < response.data.length; i++) {
                    this.volunteers.push(response.data[i]);
                }
            })
            .catch(error => {
                console.log(error);
            });
        },
        editVolunteers(volunteer_id) {
            this.$router.push({ name: 'VolunteersUpdate', params: { volunteer_id: volunteer_id } });
        } 
    },
    mounted() {
        this.getVolunteers();
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
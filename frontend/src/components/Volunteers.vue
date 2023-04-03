<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container1"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Volunteer Name</th>
                        <th style="width:5%" scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="volunteer in volunteers"
                        @click="editVolunteers(volunteer.volunteer_id)">
                            <td style="text-align:left">{{ volunteer.first_name }} {{ volunteer.last_name }}</td>
                            <!-- This v-if statement needs to check if the value is null and if it is display a 0 if it isnt then display the value-->
                            <td v-if="volunteer.total_hours == null">0</td>
                            <td v-else>{{ volunteer.total_hours }}</td>
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

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
}
.table td {
    word-wrap: break-word;
    min-width: 160px;
    max-width: 160px;
}
</style>
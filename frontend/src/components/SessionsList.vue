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
                        <th scope="col">Session Date</th>
                        <th scope="col">Event</th>
                        <th scope="col">Organization</th>
                        <th scope="col">Start Time</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="sessions in sessions"
                        @click="editSessions(sessions.session_id)">
                            <td>{{ sessions.volunteer_name }}</td>
                            <td>{{ sessions.session_date }}</td>
                            <td>{{ sessions.event_name }}</td>
                            <td>{{ sessions.org_name }}</td>
                            <td>{{ sessions.time_in }}</td>
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
            sessions:[]
        };

    },
    methods: {
        submitForm() {
        },
        getSession() {
            axios.get('http://127.0.0.1:5000/read_sessions')
            .then(response => {
                // iterate through JSON response and add sessions to sessions array
                for (var i = 0; i < response.data.length; i++) {
                    this.sessions.push(response.data[i]);
                }
            })
            .catch(error => {
                console.log(error);
            });
        },
        editSessions(session_id) {
            this.$router.push({ name: 'SessionsUpdate', params: 
            { session_id: session_id } });
        }
    },
    mounted() {
        this.getSession();

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
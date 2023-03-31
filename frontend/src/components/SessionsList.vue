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
                        <th scope="col">Session Comments</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="session in sessions" 
                            :key="session.session_id"
                            @click="editSessions(session.session_id)" 
                            :style="{ cursor: 'pointer' }"
                            :class="{ 'hoverRow': hoverId === session.session_id }"
                            @mouseenter="hoverId = session.session_id"
                            @mouseleave="hoverId = null"
                        >
                            <td>{{ session.volunteer_name }}</td>
                            <td>{{ session.session_date }}</td>
                            <td>{{ session.event_name }}</td>
                            <td>{{ session.org_name }}</td>
                            <td>{{ session.time_in }}</td>
                            <td>{{ session.session_comment }}</td>
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
            sessions:[],
            hoverId: null,
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

.hoverRow {
    background-color: rgba(230, 231, 235, 1);
    transition: background-color 0.3s ease-in-out;
  }
</style>
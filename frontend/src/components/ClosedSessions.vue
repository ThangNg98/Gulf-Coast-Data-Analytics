<template>
    <main>
    <div>
        <h2 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> <router-link class="" to="/admin/sessions_list">{{ msg }}</router-link> | <router-link class="" to="/admin/closed_sessions">{{ msg2 }}</router-link> </h2>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> Closed Sessions </h1>
    </div>
    <div class="container"> 
        
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 50%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col">Volunteer Name</th>
                        <th scope="col">Session Date</th>
                        <th scope="col">Event</th>
                        <th scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        <th scope="col">Time Out</th>
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
                            <td>{{ session.time_out }}</td>
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
    name: 'ClosedSessions',
    data() {
        return {
            msg : "Active",
            msg2 : "Closed",
            sessions:[],
            hoverId: null,
        };
    },
    methods: {
        submitForm() {
        },
        getSession() {
            axios.get('http://127.0.0.1:5000/read_closed_sessions')
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

<style scoped>
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

.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #adb5bd !important;
}
</style>
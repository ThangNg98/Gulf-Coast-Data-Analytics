<template>
    <main>
    <div>
        <h2 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> <router-link class="" to="/admin/sessions_list">{{ msg }}</router-link> | <router-link class="" to="/admin/closed_sessions">{{ msg2 }}</router-link> </h2>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> Closed Sessions </h1>
    </div>
    <div class="container"> 
        
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 20%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy ='volunteer_name'" scope="col">Volunteer Name</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='session_date'" scope="col">Session Date</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='event_name'" scope="col">Event</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='org_name'" scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        <th scope="col">Time Out</th>
                        <th scope="col">Total Hours</th>
                        <th scope="col">Session Comments</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="session in sortedItems" 
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
                            <td>{{ session.total_hours }}</td>
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
            msg : "Open",
            msg2 : "Closed",
            sessions:[],
            hoverId: null,
            sortBy: 'volunteer_name',
            sortDesc: false
        };
    },
    computed: {
        sortedItems() {
            const field = this.sortBy;
            const order = this.sortDesc ? -1 : 1;

            // Make a copy of the original array to avoid modifying the original data
            const sessions = this.sessions;

            // Sort the array by the specified field and order
            sessions.sort((a, b) => {
                if (a[field] < b[field]) return -1 * order;
                if (a[field] > b[field]) return 1 * order;
                return 0;
      });

      return sessions;
    }
},
    methods: {
        submitForm() {
        },
        getSession() {
            axios.get('https://llc.onrender.com/read_closed_sessions')
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
  width: 100%;
}

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}
</style>
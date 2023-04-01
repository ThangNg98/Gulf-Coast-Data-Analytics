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
                        <th scope="col">Event Name</th>
                        <th scope="col">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                        @click="editEvent(event.event_id)"
                        v-for="event in events" >
                            <td>{{ event.event_name }}</td>
                            <td>{{ event.event_description }}</td>
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
            events: []
        }
    },
    methods: {
        submitForm() {
        },
        getEvents() {
            axios.get('http://127.0.0.1:5000/read_events')
            .then(response => {
                // iterate through JSON response and add events to events array
                for (var i = 0; i < response.data.length; i++) {
                    this.events.push(response.data[i]);
                }
            })
            .catch(error => {
                console.log(error);
            });
        },
        editEvent(event_id) {
            this.$router.push({ name: 'EventsUpdate', params: 
            { event_id: event_id } });
        }
    },
    mounted() {
        this.getEvents();
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
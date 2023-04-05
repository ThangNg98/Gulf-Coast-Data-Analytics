<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container1 table-wrapper"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col">Event Name</th>
                        <th scope="col">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                        @click="editEvent(event.event_id)"
                        :key="event.event_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === event.event_id }"
                        @mouseenter="hoverId = event.event_id"
                        @mouseleave="hoverId = null"
                        v-for="event in events" >
                            <td style="text-align:left">{{ event.event_name }}</td>
                            <td style="text-align:left">{{ event.event_description }}</td>
                        </tr>
                    </tbody>
                </table>
        </div>
        <div style="margin-top: 2rem;margin-left: 30%">
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
            events: [],
            hoverId: null,
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

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}
.table td {
    word-wrap: break-word;
    min-width: 120px;
    max-width: 160px;
}

.hoverRow {
    background-color: rgba(230, 231, 235, 1);
    transition: background-color 0.3s ease-in-out;
  }

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}

.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}
</style>
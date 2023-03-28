<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Session Date</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="this.session_info.session_date">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Comment</label>
                        <textarea class="form-control" id="exampleFormControlInput1" v-model="this.session_info.session_comment"></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Time In</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="this.session_info.time_in">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Time Out</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="this.session_info.time_out">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Event</label>
                        <div>
                            <select class="form-select" v-model="session_info.event_id">
                                <option value="">Select an Event</option>
                                <option v-for="event in events" :key="event.event_id" :value="event.event_id">{{ event.event_name }}</option>
                            </select>
                            </div>
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Organization</label>
                        <input type="text" class="form-control" style="max-width: 49%" id="exampleFormControlInput1" placeholder="UH Garden Team">
                    </div>
                </div>
            </div>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/sessions_list"> Back to Sessions</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem">Update </button>
                <button type="submit" class="btn btn-danger" >Delete</button>
            </div>
        </form>
        <p>orgs: {{ orgs }}</p>
        <p>events: {{ events }}</p>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'SessionsUpdate',
    data() {
        return {
            msg : "[Volunteer Name]'s Active Session",
            session_info: {
                session_id: 1,
                time_in: '2099-10-10 15:15:15',
                time_out: '2099-10-10 15:15:15',
                session_date: '2099-10-10',
                session_comment: 'this is a COMMENT',
                org_id: 3,
                event_id: 4,
                session_status_id: 1,
                volunteer_id: 3
            },
            orgs: [],
            events: []
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:5000/read_orgs')
            .then(response => {
                // iterate through JSON response and add orgs to orgs array
                for (var i = 0; i < response.data.length; i++) {
                    this.orgs.push({
                        org_name: response.data[i].org_name,
                        org_id: response.data[i].org_id
                    });
                }
            })
            .catch(error => {
                console.log(error);
            });
        axios.get('http://127.0.0.1:5000/read_events')
        .then(response => {
            // iterate through JSON response and add orgs to orgs array
            for (var i = 0; i < response.data.length; i++) {
                this.events.push({
                    event_name: response.data[i].event_name,
                    event_id: response.data[i].event_id
                });
            }
        })
        .catch(error => {
            console.log(error);
        });
        
    },
    methods: {
        submitForm() {
            alert('Submitted')
        }
    }
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
  text-align: left

}
</style>
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
                        <br>
                        <input type="date" id="date" v-model="session_info.session_date" @input="formatDate">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Comment</label>
                        <textarea class="form-control" id="exampleFormControlInput1" v-model="session_info.session_comment"></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Time In</label>
                        <div class="input-group mb-3">
                            <input type="time" class="form-control" placeholder="hh:mm" aria-label="Time" aria-describedby="basic-addon1" v-model="session_info.time_in">
                        </div>
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Time Out</label>
                        <div class="input-group mb-3">
                            <input type="time" class="form-control" placeholder="hh:mm:ss" aria-label="Time" aria-describedby="basic-addon1" v-model="session_info.time_out">
                        </div>
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
                            <div>
                            <select class="form-select" v-model="session_info.org_id">
                                <option value="">Select an Organization</option>
                                <option v-for="org in orgs" :key="org.org_id" :value="org.org_id">{{ org.org_name }}</option>
                            </select>
                            </div>
                        </div>
                    </div>
                </div>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/sessions_list"> Back to Sessions</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" @click="updateButtonClicked = true">Update </button>
                <button type="submit" class="btn btn-danger" @click="deleteButtonClicked=true">Delete</button>
            </div>
        </form>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'SessionsUpdate',
    data() {
        return {
            msg : "Volunteer's Active Session",
            session_info: {
                session_id: 2,
                time_in: null,
                time_out: null,
                session_date: null,
                session_comment: null,
                full_name: null,
                org_id: null,
                event_id: null
            },
            updateButtonClicked: false,
            deleteButtonClicked: false,
            events: [],
            orgs: [],
            temp_time_in: null
        };
    },
    mounted() {
        this.getSession(); //need to acocunt for how many events and orgs there are. the more events and orgs the longer the delay
        setTimeout(() => {
            this.getEvents();
        }, 100); // delay of 0.5 seconds
        setTimeout(() => {
            this.getOrgs();
        }, 200); // delay of 1 second
    },
    methods: {
        submitForm() {
            if (this.updateButtonClicked == true){
                this.updateButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/update_session', this.session_info)
                .then(()=>{
                    this.session_info={}
                    alert('Session updated')
                    this.$router.push('/admin/sessions_list')
                })
                .catch(()=>{
                    console.log(error);
                });
            }
            else if (this.deleteButtonClicked = true){
                this.deleteButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/delete_session', this.session_info)
                .then(()=>{
                    this.session_info = {}
                    alert('Session deleted')
                    this.$router.push('/admin/sessions_list')
                })
                .catch(()=>{
                    console.log(error);
                });
            }
        },
        getSession() {
            axios.get(`http://127.0.0.1:5000/read_session/2`)
                .then(response => {
                    console.log('response:', response.data);
                    this.session_info.session_id = response.data[0].session_id;
                    this.session_info.time_in = response.data[0].time_in;
                    console.log('response.data[0].time_in:', response.data[0].time_in)
                    this.session_info.time_out = response.data[0].time_out;
                    this.session_info.session_date = response.data[0].session_date;
                    //response.data[0].session_date;
                    this.session_info.session_comment = response.data[0].session_comment;
                    this.session_info.full_name = response.data[0].full_name;
                    this.session_info.org_id = response.data[0].org_id;
                    this.session_info.event_id = response.data[0].event_id;
                    // //format datetime
                    // const datetime = new Date(this.session_info.time_in);
                    // this.temp_time_in = datetime.toISOString().slice(0, 19).replace('T', ' ')
            })
                .catch(error => {
                    console.log(error);
            });
        },
        getEvents() {
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
        },
        getOrgs() {
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
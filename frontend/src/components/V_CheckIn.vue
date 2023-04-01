<template>
    <div class="container">
    <div class="d-flex justify-content-center">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
            <!--event selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Event Select" name="eventSelect" v-model="session.event_id">
                <option :value=null>-</option>
                <option v-for="event in events" :value="event.event_id" :key="event.event_id">
                    {{ event.event_name }}
                </option>
                </select>
            </div>
            <p>session.event_id {{ session.event_id }}</p>
            <!--org selection-->
            <div class="d-flex justify-content-between">
                <label for="orgSelect"><h4>Organization</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="session.org_id">
                    <option :value=null>-</option>
                    <option v-for="org in orgs" :value="org.org_id" :key="org.org_id">{{ org.org_name }}</option>
                </select>
            </div>
            <p>session.org_id: {{session.org_id}}</p>
        </div>
    </div>
    <br>
    <!--checkin checkout-->
    <div class="d-flex justify-content-center mb-4">
        <div class="d-inline-flex flex-column border border-dark" style="width:300px;">
                <div :class="{ 'text-muted': checkedIn }" class="p-2 float-start">
                    <div class="d-inline-block float-start p-2">You are checked out</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="checkedInButton = true; getTime(); create_session(); checkedIn = !checkedIn" :disabled="checkedIn">Check In</button></div>
                </div>
                <div :class="{ 'text-muted': !checkedIn }" class="p-2 float-end">
                    <div class="d-inline-block float-start p-2">You are checked in</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="checkedOutButton = true; getTime(); update_session_axios(); checkedIn = !checkedIn;" :disabled="!checkedIn">Check Out</button></div>
                </div>
        </div>
    </div>
    <p>events: {{ this.events }}</p>
    <p>orgs: {{ this.orgs }}</p>
    <p>session.volunteer_id: {{ session.volunteer_id }}</p>
    </div>
</template>
<script>
import axios from 'axios';
import { useVolunteerPhoneStore } from '../stores/VolunteerPhoneStore'

export default {
    data() {
        return {
            checkedIn: false, //checked in state
            orgs: [],
            events: [],
            session: {
                session_id: 6,
                time_in: null,//now.time(),
                time_out: null,
                session_date: this.getDate(),//now.date(), 
                session_comment: "CURRENT TEST 10:35pm",
                org_id: null,
                event_id: null,
                session_status_id: 1,
                volunteer_id: useVolunteerPhoneStore().volunteerID // volunteer id needs to be stored and pulled
            },
            checkedInButton: false,
            checkedOutButton: false
        }
    },
    mounted() {
        this.getEvents()
        setTimeout(() => {
            this.getOrgs()
        }, 250)        
    },
    methods: {
        getEvents() {
            axios
                .get('http://127.0.0.1:5000/read_events')
                .then((response) => {
                    console.log('read_events response:', response)
                    this.events = response.data.map(event => ({ event_id: event.event_id, event_name: event.event_name }));
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        getOrgs() {
            axios
                .get('http://127.0.0.1:5000/read_orgs')
                .then((response) => {
                    console.log('read_orgs response:', response)
                    this.orgs = response.data.map(org => ({org_id: org.org_id, org_name: org.org_name}));
                })
                .catch(error => {
                    console.log(error)
                })
        },
        create_session() {
            this.time_in = this.getTime();
            this.create_session_axios(); //create session
        },
        async create_session_axios() { //call axios
            axios
                .post('http://127.0.0.1:5000/create_session', this.session)
                .then(() => {
                })
                .catch((error) => {
                    console.log(error);
          });
          console.log("create_session success");
        },
        async update_session_axios() { //call axios
            console.log('this.session:', this.session)
            axios
                .post('http://127.0.0.1:5000/check_out', this.session)
                .then(() => {
                    this.session = {}
                })
                .catch((error) => {
                    console.log(error);
          });
          console.log("update_session success");
        },
        getDate() {
            var today = new Date();
            today.setHours( today.getHours()+(today.getTimezoneOffset()/-60) );
            return today.toJSON().slice(0, 10)
        },
        getTime() {
            // var today = new Date();
            // today.setHours( today.getHours()+(today.getTimezoneOffset()/-60) );
            // var firstHalf = today.toJSON().slice(0,10);
            // var secondHalf = today.toJSON().slice(11,19);
            // var full = firstHalf + " " + secondHalf;
            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            const seconds = now.getSeconds().toString().padStart(2, '0');
            const mysqlTime = `${hours}:${minutes}:${seconds}`;
            if (this.checkedInButton == true) {
                console.log('check in button called')
                this.checkedInButton = false
                this.session.time_in = mysqlTime
            }
            else if (this.checkedOutButton == true) {
                this.checkedOutButton = false
                this.session.time_out = mysqlTime
            }
        }
    }
}
</script>
<template>
    <div class="container">
    <div class="d-flex justify-content-center">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
            <!--event selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Event Select" name="eventSelect" v-model="session.event_id" :disabled="alreadyCheckedIn">
                <option :value=null>-</option>
                <option v-for="event in events" :value="event.event_id" :key="event.event_id">
                    {{ event.event_name }}
                </option>
                </select>
            </div>
            <!--org selection-->
            <div class="d-flex justify-content-between">
                <label for="orgSelect"><h4>Organization</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="session.org_id" :disabled="alreadyCheckedIn">
                    <option :value=null>-</option>
                    <option v-for="org in orgs" :value="org.org_id" :key="org.org_id">{{ org.org_name }}</option>
                </select>
            </div>
        </div>
    </div>
    <br>
    <!--checkin checkout-->
    <div class="d-flex justify-content-center mb-4">
        <div class="d-inline-flex flex-column border border-dark" style="width:300px;">
                <div :class="{ 'text-muted': alreadyCheckedIn }" class="p-2 float-start">
                    <div class="d-inline-block float-start p-2">You are checked out</div><div 
                    class="d-inline-block float-end h-100" 
                    style="width:100px"><button class="w-100 h-100" type="button" 
                    @click="checkedInButton = true; getTime(); create_session(); alreadyCheckedIn = !alreadyCheckedIn" 
                    :disabled="alreadyCheckedIn">Check In</button></div>
                </div>
                <div :class="{ 'text-muted': !alreadyCheckedIn }" class="p-2 float-end">
                    <div class="d-inline-block float-start p-2">You are checked in</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="checkedOutButton = true; getTime(); update_session_axios(); alreadyCheckedIn = !alreadyCheckedIn;" :disabled="!alreadyCheckedIn">Check Out</button></div>
                </div>
        </div>
    </div>
    <h2 style="text-align: center"> Current Session</h2>
    <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Event Name</th>
                        <th scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td> {{ this.event_name }}</td>
                            <td> {{ this.org_name }}</td>
                            <td> {{ this.time_in }}</td>
                        </tr>
                    </tbody>
                </table>
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
                session_id: null,
                time_in: null,//now.time(),
                time_out: null,
                session_date: this.getDate(),//now.date(), 
                session_comment: "CURRENT TEST 10:35pm",
                org_id: null, 
                event_id: null, 
                session_status_id: "1",
                volunteer_id: useVolunteerPhoneStore().volunteerID // volunteer id needs to be stored and pulled
            },
            checkedInButton: false,
            checkedOutButton: false,
            alreadyCheckedIn: false,
            event_name: null,
            org_name: null,
            time_in: null
        }
    },
    mounted() {
        setTimeout(() => {
            this.checkRecent();
        }, 500); 
        setTimeout(() => {
            this.getEvents();
        }, 1000); 
        setTimeout(() => {
            this.getOrgs();
        }, 1500); 
        setTimeout(() => {
            axios
            .get(`http://127.0.0.1:5000/current_session/${this.session.session_id}`)
                    .then((response) => {
                        this.event_name = response.data[0].event_name
                        this.org_name = response.data[0].org_name
                        this.time_in = response.data[0].time_in
                    })


            },2000);
    },
    methods: {
        checkRecent() {
            axios
                .get(`http://127.0.0.1:5000/check_most_recent/${this.session.volunteer_id}`)
                .then((response) => {
                    if (response.data[0]) {
                        const temp_checkedIn = response.data[0].time_out
                        if (temp_checkedIn == '1') {
                            this.session.session_id = response.data[0].session_id
                            this.session.org_id = response.data[0].org_id
                            this.session.event_id = response.data[0].event_id
                            this.alreadyCheckedIn = true
                        }
                        else if (temp_checkedIn == '2') {
                            this.alreadyCheckedIn = false
                        }
                    }
                    else {
                        this.alreadyCheckedIn = false
                    }
                })
                .catch((error) => {
                  console.log(error)
                })
        },
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
                    console.log(this.session.event_id)
                })
                .catch((error) => {
                    console.log(error);
            });
            console.log("create_session success");
            setTimeout(() => {
                axios
                    .get(`http://127.0.0.1:5000/check_most_recent/${this.session.volunteer_id}`)
                    .then((response) => {
                        this.session.session_id = response.data[0].session_id
                    })
            }, 500); 
            setTimeout(() => {
                axios
                .get(`http://127.0.0.1:5000/current_session/${this.session.session_id}`)
                        .then((response) => {
                            this.event_name = response.data[0].event_name
                            this.org_name = response.data[0].org_name
                            this.time_in = response.data[0].time_in
                        })


            },1000);
        },
        async update_session_axios() { //call axios
            console.log('this.session:', this.session)
            axios
                .post('http://127.0.0.1:5000/check_out', this.session)
                .then(() => {
                    this.session.org_id = null
                    this.session.event_id = null
                    this.event_name = null
                    this.org_name = null
                    this.time_in = null
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
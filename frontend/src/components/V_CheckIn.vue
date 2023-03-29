<template>
    <div class="container">
    <div class="d-flex justify-content-center">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
            <!--event selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Event Select" name="eventSelect" v-model="inputEvent">
                    <option selected value="none">None</option>
                    <option v-for="event in eventNames" :key="event">{{ event }}</option>
                </select>
            </div>
            <!--org selection-->
            <div class="d-flex justify-content-between">
                <label for="orgSelect"><h4>Organization</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="inputOrg">
                    <option selected value="none">None</option>
                    <option v-for="org in orgNames" :key="org">{{ org }}</option>
                </select>
            </div>
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
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            checkedIn: false, //checked in state
            inputOrg:"", //currently selected organization
            orgNames: ['org1', 'org2', 'org3'], //placeholder for org names list from api
            inputEvent:"", //currently selected event
            eventNames: ['event1', 'event2', 'event3'], //placeholder for event names list from api
            //test data
            session: {
                session_id: 6,
                time_in: null,//now.time(),
                time_out: null,
                session_date: this.getDate(),//now.date(), 
                session_comment: "CURRENT TEST 10:35pm",
                org_id: "1", 
                event_id: "2", 
                session_status_id: "1",
                volunteer_id: "2" // volunteer id needs to be stored and pulled
            },
            checkedInButton: false,
            checkedOutButton: false
            
            
        }
    },
    methods: {
        create_session() {
            console.log("create_session");
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
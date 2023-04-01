<template>
    <div class="container">
    <div class="d-flex justify-content-center" v-if="!checkedIn">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
            <!--comment section-->
            <div>
                <label class="d-block" for="comment_section"><h4>Comments</h4></label>
                <textarea class="d-inline-block" placeholder="Enter a comment." name="comment_section" rows="4" cols="40" maxlength="255" v-model="session.session_comment"></textarea>
            </div>
            <br>
            <!--event selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Event Select" name="eventSelect" v-model="inputEvent">
                    <option selected value="none">None</option>
                    <option v-for="event in eventNames">{{ event }}</option>
                </select>
            </div>
            <!--org selection-->
            <div class="d-flex justify-content-between">
                <label for="orgSelect"><h4>Organization</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="inputOrg">
                    <option selected value="none">None</option>
                    <option v-for="org in orgNames">{{ org }}</option>
                </select>
            </div>
        </div>
    </div>
    <div v-if="checkedIn">
        <table class="table">
            <thead>
                <tr>
                <th scope="col">Time In</th>
                <th scope="col">Total Time</th>
                <th scope="col">Organization</th>
                <th scope="col">Event</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <!--REPLACE WITH CORRECT VALUES-->
                <td>{{ this.session_creation_time.slice(11) }}</td>
                <td>Elapsed Time</td> <!--(new Date() - session date) converted to time string-->
                <td>{{  this.inputOrg }}</td> <!--get input org name-->
                <td>{{ this.inputEvent }}</td> <!--get input event name-->
                </tr>
            </tbody>
        </table>
    </div>
    <br>
    <!--checkin checkout-->
    <div class="d-flex justify-content-center mb-4">
        <div class="d-inline-flex flex-column border border-dark" style="width:300px;">
                <div :class="{ 'text-muted': checkedIn }" class="p-2 float-start">
                    <div class="d-inline-block float-start p-2">You are checked out</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="create_session(); this.session_creation_time = getTime(); checkedIn = !checkedIn;" :disabled="checkedIn">Check In</button></div>
                </div>
                <div :class="{ 'text-muted': !checkedIn }" class="p-2 float-end">
                    <div class="d-inline-block float-start p-2">You are checked in</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="checkedIn = !checkedIn" :disabled="!checkedIn">Check Out</button></div>
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
            inputOrg:"None", //currently selected organization
            orgNames: ['org1', 'org2', 'org3'], //placeholder for org names list from api
            inputEvent:"None", //currently selected event
            eventNames: ['event1', 'event2', 'event3'], //placeholder for event names list from api
            //test data
            session_creation_time: '',
            session: {
                time_in: this.getTime(),//now.time(),
                session_date: this.getDate(),//now.date(), 
                session_comment: "",
                org_id: "1", 
                event_id: "2", 
                session_status_id: "1",
                volunteer_id: "3" // volunteer id needs to be stored and pulled
            },
            
        }
    },
    methods: {
        create_session() {
            this.time_in = this.getTime();
            this.create_session_axios(); //create session
        },
        async create_session_axios() { //call axios
            axios
                .post('http://127.0.0.1:5000/create_session', this.session)
                .then(() => {
                    this.session = {}
                })
                .catch((error) => {
                    console.log(error);
          });
          console.log("create_session success");
        },
        getDate() {
            var today = new Date();
            today.setHours( today.getHours()+(today.getTimezoneOffset()/-60) );
            return today.toJSON().slice(0, 10)
        },
        getTime() {
            var today = new Date();
            today.setHours( today.getHours()+(today.getTimezoneOffset()/-60) );
            var firstHalf = today.toJSON().slice(0,10);
            var secondHalf = today.toJSON().slice(11,19);
            var full = firstHalf + " " + secondHalf;
            return full
        }
    }
}
</script>
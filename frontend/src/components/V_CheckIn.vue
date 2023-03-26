<template>
    <div class="container">
    <div class="d-flex justify-content-center">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
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
    <br>
    <!--checkin checkout-->
    <div class="d-flex justify-content-center mb-4">
        <div class="d-inline-flex flex-column border border-dark" style="width:300px;">
                <div :class="{ 'text-muted': checkedIn }" class="p-2 float-start">
                    <div class="d-inline-block float-start p-2">You are checked out</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="create_session(); checkedIn = !checkedIn;" :disabled="checkedIn">Check In</button></div>
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
            inputOrg:"", //currently selected organization
            orgNames: ['org1', 'org2', 'org3'], //placeholder for org names list from api
            inputEvent:"", //currently selected event
            eventNames: ['event1', 'event2', 'event3'], //placeholder for event names list from api
            //test data
            time_in: "",
            time_out: "",
            session_date: "2023-03-26", 
            session_comment: "CURRENT TEST",
            org_id: "1", 
            event_id: "2", 
            session_staus_id: "1"
        }
    },
    methods: {
        create_session() {
            console.log("create_session")
            this.create_session_axios();
        },
        async create_session_axios(time_in, time_out, session_date, session_comment, org_id, event_id, session_staus_id) {
            const response = await axios.post('http://localhost:5000/create_session', {time_in, time_out, session_date, session_comment, org_id, event_id, session_staus_id});
            console.log(response.data);
            return response.data;
        }
    }
}
</script>
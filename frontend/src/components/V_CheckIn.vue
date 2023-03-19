<template>
    <!--event selection-->
    <div class="mb-3">
        <label for="eventSelect"><h4>Event</h4></label>
        <select class="form-select border-2 border-dark rounded-0 mb-3 ms-2 w-auto d-inline-block" aria-label="Event Select" name="eventSelect" v-model="inputEvent">
            <option selected value="none">None</option>
            <option v-for="event in eventNames">{{ event }}</option>
        </select>
    </div>
    <!--org selection-->
    <div class="mb-3">
        <label for="orgSelect"><h4>Organization</h4></label>
        <select class="form-select border-2 border-dark rounded-0 mb-3 ms-2 w-auto d-inline-block" aria-label="Org Select" name="orgSelect" v-model="inputOrg">
            <option selected value="none">None</option>
            <option v-for="org in orgNames">{{ org }}</option>
        </select>
    </div>
    <!--checkin checkout-->
    <div class="d-flex justify-content-center">
        <div class="border border-dark text-start">
            <div :class="{ 'text-muted': !checkedIn }" class="row">
                <div class="col ps-4">You are checked in </div><div class="col"><button class="w-100 h-100" type="button" @click="checkedIn = !checkedIn" :disabled="!checkedIn">Check Out</button></div>
            </div>
            <div :class="{ 'text-muted': checkedIn }" class="row">
                <div class="col ps-4">You are checked out </div><div class="col"><button class="w-100 h-100" type="button" @click="checkedIn = !checkedIn" :disabled="checkedIn">Check In</button></div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            checkedIn: true, //checked in state
            inputOrg:"", //currently selected organization
            orgNames: ['org1', 'org2', 'org3'], //placeholder for org names list from api
            inputEvent:"", //currently selected event
            eventNames: ['event1', 'event2', 'event3'], //placeholder for event names list from api

        }
    }
}
</script>
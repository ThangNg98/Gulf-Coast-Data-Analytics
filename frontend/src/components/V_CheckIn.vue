<template>
    <div class="container">
    <div class="d-flex justify-content-center">
        <div class="d-inline-flex flex-column w-25 text-start" style="min-width:300px">
            <!--event selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Event Select" name="eventSelect" v-model="session.event_id" :disabled="alreadyCheckedIn">
                <option v-for="event in events" :value="event.event_id" :key="event.event_id">
                    {{ event.event_name }}
                </option>
                </select>
            </div>
            <!--org selection-->
            <div class="mb-3 d-flex justify-content-between">
                <label for="orgSelect"><h4>Organization</h4></label>
                <select class="form-select border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="session.org_id" :disabled="alreadyCheckedIn">
                    <option :value=null></option>
                    <option v-for="org in orgs" :value="org.org_id" :key="org.org_id">{{ org.org_name }}</option>
                </select>
            </div>

            <div class="d-flex justify-content-between">
                <label for="orgSelect"><h4>Comments</h4></label>
                <textarea style="resize:none; border-width:1px" class="border-2 border-dark rounded-0 ms-2 w-50 d-inline-block" :disabled="alreadyCheckedIn" v-model="session.session_comment">  </textarea>
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
    <div class="container" v-if="alreadyCheckedIn">
        <h2 style="text-align: center"> Current Session</h2>
        <table class="table table-bordered" style="margin:auto; text-align: center; margin-top: 2rem;">
                    <thead>
                        <tr>
                        <th scope="col">Event Name</th>
                        <th scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        <th scope="col">Comment</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td> {{ this.current_event_name }}</td>
                            <td> {{ this.current_org_name }}</td>
                            <td> {{ this.session.time_in }}</td>
                            <td> {{ this.session.session_comment }}</td>
                        </tr>
                    </tbody>
                </table>
    </div>
    </div>
    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>
</template>
<script>
import axios from 'axios';
import { useVolunteerPhoneStore } from '../stores/VolunteerPhoneStore'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { checkMostRecentAPI, getEventsAPI, getOrgsAPI, createSessionAPI, checkOutAPI } from '../api/api.js'

export default {
    components: {
        LoadingModal
    },
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
                session_comment: '',
                org_id: null, 
                event_id: null, 
                session_status_id: "1",
                volunteer_id: useVolunteerPhoneStore().volunteerID // volunteer id needs to be stored and pulled
            },
            checkedInButton: false,
            checkedOutButton: false,
            alreadyCheckedIn: false,
            current_event_name: null,
            current_org_name: null,
            time_in: null,
            isLoading: false
        }
    },
    mounted() {
        const loadingStore = useLoadingStore()
        console.log('loadingStore:', loadingStore)
        this.loadData();
    },
    methods: {
        async loadData() {
        this.isLoading = true;
        try {
            await this.checkMostRecent();
            await this.getEvents();
            await this.getOrgs();
            if (this.alreadyCheckedIn) {
                    this.getCurrentInfo()
            }
        } catch (error) {
            console.log(error);
        }
        this.isLoading = false;
        },
        async checkMostRecent() {
            try {
                const result = await checkMostRecentAPI(this.session.volunteer_id);
                console.log('result:', result)
                this.alreadyCheckedIn = result.alreadyCheckedIn;
                this.session.session_id = result.session?.session_id;
                this.session.org_id = result.session?.org_id;
                this.session.event_id = result.session?.event_id;
                this.session.time_in = result.session?.time_in;
                this.session.session_comment = result.session?.session_comment;
                console.log('this.alreadyCheckedIn:',  this.alreadyCheckedIn)
                console.log('this.session.session_id:',  this.alreadyCheckedIn)
                console.log('this.session.org_id:', this.session.org_id)
                console.log('this.session.event_id', this.session.event_id)
                console.log('this.session.time_in', this.session.time_in)
                console.log('this.session.session_comment', this.session.session_comment)
            } catch (error) {
                console.log(error)
            }
        },
        async getEvents() {
            try {
                const response = await getEventsAPI();
                this.events = response.data.map(event => ({ event_id: event.event_id, event_name: event.event_name }));
                console.log('this.events:', this.events)
            } catch (error) {
                console.log(error)
            }
        },
        async getOrgs() {
            try {
                const response = await getOrgsAPI();
                this.orgs = response.data.map(org => ({org_id: org.org_id, org_name: org.org_name}));
                console.log('this.orgs:', this.orgs)
            } catch (error) {
                console.log(error)
            }
        },
        async create_session() {
            this.time_in = this.getTime();
            console.log('this.session:', this.session)
            try {
                await createSessionAPI(this.session)
                this.getCurrentInfo()
                console.log('create_session success')
            } catch (error) {
                console.log(error);
            }
        },
        getCurrentInfo() {
            console.log('this.session.event_id:', this.session.event_id)
            console.log('this.events:', this.events)
            const event = this.events.find(e => e.event_id === this.session.event_id)
            this.current_event_name = event.event_name
            const org = this.orgs.find(o => o.org_id === this.session.org_id)
            if (org) {
                this.current_org_name = org.org_name
            } else {
                this.current_org_name = ''
            }
        },
        async update_session_axios() { //call axios
            this.isLoading = true;
            await this.update_session_axios_1();
            await this.update_session_axios_2();
            this.isLoading = false;
        },
        async update_session_axios_1() {
            console.log('this.session.volunteer_id:', this.session.volunteer_id)
            try {
                const result = await checkMostRecentAPI(this.session.volunteer_id);
                console.log('result from update 1', result)
                this.session.session_id = result.session.session_id
            } catch(error) {
                console.log(error)
            }
        },
        async update_session_axios_2() {
            try {
                console.log('this.session:', this.session)
                await checkOutAPI(this.session);
                this.session.org_id = null
                this.session.event_id = null
                this.session.session_comment = null
                this.current_event_name = null
                this.current_org_name = null
                console.log("update_session success");
            } catch (error) {
                console.log(error)
            }
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

<style scoped>

@media only screen and (min-width: 768px) {
    .container {
      margin: auto;
      padding-left: auto;
      padding-right: auto;
      width: 50%
    }
    }

@media only screen and (min-width: 992px) {
.container {
    margin: auto;
    padding-left: auto;
    padding-right: auto;
    width: 40%
}
}

@media only screen and (min-width: 1200px) {
.container {
    margin: auto;
    padding-left: auto;
    padding-right: auto;
    width: 35%
}
}
</style>
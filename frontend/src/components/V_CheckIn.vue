<template>
    <div v-if="!isLoading">
        <div class="d-flex justify-content-center">
            <div class="d-inline-flex flex-column w-75 text-start" style="min-width:300px">
                <div v-if="errors.eventSelect" style="color: #dc3545;">
                    Event is required
                </div>
                <!--event selection-->
                <div class="mb-3 d-flex flex-column">
                    <label for="eventSelect" class="text-start"><h4>Event</h4></label>
                    <select class="form-select border-2 border-dark rounded-0 w-100 d-inline-block" aria-label="Event Select" name="eventSelect" ref="eventSelect" v-model="session.event_id" :disabled="alreadyCheckedIn || confirmModal" :class="{ 'is-invalid': errors.eventSelect }">
                    <option v-for="event in events" :value="event.event_id" :key="event.event_id">
                        {{ event.event_name }}
                    </option>
                    </select>
                </div>
                <!--org selection-->
                <div class="mb-3 d-flex flex-column">
                    <label for="orgSelect"><h4>Organization</h4></label>
                    <select class="form-select border-2 border-dark rounded-0 w-100 d-inline-block" aria-label="Org Select" name="orgSelect" v-model="session.org_id" :disabled="alreadyCheckedIn || confirmModal">
                        <option :value=null></option>
                        <option v-for="org in orgs" :value="org.org_id" :key="org.org_id">{{ org.org_name }}</option>
                    </select>
                </div>

                <div class="d-flex flex-column">
                    <label for="orgSelect"><h4>Comments</h4></label>
                    <textarea style="resize:none; border-width:1px" class="border-2 border-dark rounded-0 w-100 d-inline-block" rows="3" :disabled="alreadyCheckedIn || confirmModal" v-model="session.session_comment">  </textarea>
                </div>
            </div>
        </div>
        <br>
        <!--checkin checkout-->
        <div class="d-flex justify-content-center mb-4">
            <div class="d-inline-flex flex-column border border-dark" style="width:300px;">
                    <div :class="{ 'text-muted-custom': alreadyCheckedIn }" class="p-2 float-start">
                        <div class="d-inline-block float-start p-2">You are checked out</div><div 
                        class="d-inline-block float-end h-100" 
                        style="width:100px"><button class="w-100 h-100" type="button" 
                        @click="checkedInButton = true; getTime(); create_session();" 
                        :disabled="alreadyCheckedIn || confirmModal">Check In</button></div>
                    </div>
                    <div :class="{ 'text-muted-custom': !alreadyCheckedIn }" class="p-2 float-end">
                        <div class="d-inline-block float-start p-2">You are checked in</div><div class="d-inline-block float-end h-100" style="width:100px"><button class="w-100 h-100" type="button" @click="checkedOutButton = true; getTime(); update_session_axios();" :disabled="!alreadyCheckedIn || confirmModal">Check Out</button></div>
                    </div>
            </div>
        </div>
        <!--current session-->
        <div class="d-flex justify-content-center" v-if="alreadyCheckedIn">
            <div class="d-inline-flex flex-column w-75 text-start mt-1" style="min-width:300px">
            <h2 style="text-align: center"> Current Session</h2>
            <div class="table-responsive">
                <table class="table table-hover table-bordered" style="margin:auto; text-align: start; margin-top: 1rem; min-width: 300px;">
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
                            <td> {{ this.timeInDisplay }}</td>
                            <td> {{ this.session.session_comment }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            </div>
        </div>
    </div>    

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>
</template>
<script>
import axios from 'axios';
import { useVolunteerPhoneStore } from '../stores/VolunteerPhoneStore'
import ConfirmModal from './ConfirmModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { checkMostRecentAPI, getEventsAPI, getOrgsAPI, createSessionAPI, checkOutAPI } from '../api/api.js'

export default {
    components: {
        ConfirmModal,
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
                volunteer_id: useVolunteerPhoneStore().volunteerID // volunteer id stored and pulled
            },
            checkedInButton: false,
            checkedOutButton: false,
            alreadyCheckedIn: false,
            current_event_name: null,
            current_org_name: null,
            time_in: null,
            isLoading: false,
            errors: {},
            submitPressed: false,
            confirmModal: false,
            timeInDisplay: null,
        }
    },
    watch: {
        'session.event_id'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('eventSelect')
                } else {
                    this.addValidationStyle('eventSelect', 'Event is required.')
                }
            }
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
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        closeConfirmModal(value) {
            this.confirmModal = false
            if (value === 'yes') {
                if (this.title === 'Please Confirm Check In') {
                    this.title = '';
                    this.message = '';
                    this.create_session_call();
                } else if (this.title === 'Please Confirm Check Out') {
                    this.title = '';
                    this.message = '';
                    this.update_session_axios_call();
                }
            }
        },
        async checkMostRecent() {
            try {
                const result = await checkMostRecentAPI(this.session.volunteer_id);
                console.log('result:', result)
                this.alreadyCheckedIn = result.alreadyCheckedIn;
                this.session.session_id = result.session?.session_id ?? null;
                this.session.org_id = result.session?.org_id ?? null;
                this.session.event_id = result.session?.event_id ?? null;
                this.session.time_in = result.session?.time_in ?? null;
                this.session.session_comment = result.session?.session_comment ?? null;
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
        create_session() {
            this.submitPressed = true;
            this.errors = {};
            if (!this.session.event_id) {
                console.log('this.session.event_id', this.session.event_id)
                this.errors.eventSelect = 'Event is required.'
            }
            if (Object.keys(this.errors).length === 0) {
                console.log('Object.keys(this.errors).length', Object.keys(this.errors).length)
                this.time_in = this.getTime();
                console.log('CREATE SESSION this.session:', this.session);
                this.confirmModal = true
                this.title = 'Please Confirm Check In'
                this.message = "Are you sure you want to check in?"
            }
        },
        async create_session_call() {
            this.alreadyCheckedIn = !this.alreadyCheckedIn
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
            //format datetime
            const timeParts = this.session.time_in.split(':');
            const hours = parseInt(timeParts[0]);
            const minutes = parseInt(timeParts[1]);
            const time = new Date();
            time.setHours(hours);
            time.setMinutes(minutes);
            const options = { hour12: true, hour: 'numeric', minute: 'numeric' };
            this.timeInDisplay = time.toLocaleTimeString(navigator.language, options);
        },
        update_session_axios() {
            this.confirmModal = true
            this.title = 'Please Confirm Check Out'
            this.message = "Are you sure you want to check out?"
        },
        async update_session_axios_call() {
            this.alreadyCheckedIn = !this.alreadyCheckedIn;
            this.isLoading = true;
            await this.update_session_axios_1();
            await this.update_session_axios_2();
            this.isLoading = false;
            this.errors = {};
            this.submitPressed = false;
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
<style>
.text-muted-custom {
    color: #ddd;
}
</style>
<template>
    <div>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ session_info.full_name }}'s Active Session</h1>
    </div>
    <div class="container" style="text-align:left"> 
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Session Date</label>
                        <br>
                        <input type="date" id="date" class="form-control" v-model="session_info.session_date" @input="formatDate" :disabled="confirmModal" :class="{ 'is-invalid': errors.date }">
                        <div class="invalid-feedback">{{errors.date}}</div>
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Comment</label>
                        <textarea class="form-control" id="exampleFormControlInput1" v-model="session_info.session_comment" maxlength="255" :disabled="confirmModal"></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="timeIn" class="form-label">Time In</label>
                        <div class="input-group mb-3">
                            <input type="time" class="form-control" ref="timeIn" placeholder="hh:mm" aria-label="Time" aria-describedby="basic-addon1" v-model="session_info.time_in" :disabled="confirmModal" :class="{ 'is-invalid': errors.timeIn }">
                            <div class="invalid-feedback">{{errors.timeIn}}</div>
                        </div>
                    </div>
                    <div class="col"> 
                        <label for="timeOut" class="form-label">Time Out</label>
                        <div class="input-group mb-3">
                            <input type="time" class="form-control" ref="timeOut" placeholder="hh:mm:ss" aria-label="Time" aria-describedby="basic-addon1" v-model="session_info.time_out" :disabled="confirmModal" :class="{ 'is-invalid': errors.timeError || errors.closedSession}">
                            <div class="invalid-feedback">{{errors.timeError}}</div>
                            <div class="invalid-feedback">{{errors.closedSession}}</div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="event" class="form-label">Event</label>
                        <div>
                            <select class="form-select" ref="event" v-model="session_info.event_id" :disabled="confirmModal" :class="{ 'is-invalid': errors.event }">
                                <option value="">Select an Event</option>
                                <option v-for="event in events" :key="event.event_id" :value="event.event_id">{{ event.event_name }}</option>
                            </select>
                            <div class="invalid-feedback">{{errors.event}}</div>
                        </div>
                    </div>
                    <div class="col"> 
                            <label for="exampleFormControlInput1" class="form-label">Organization</label>
                            <div>
                            <select class="form-select" v-model="session_info.org_id" :disabled="confirmModal">
                                <option value="">Select an Organization</option>
                                <option v-for="org in orgs" :key="org.org_id" :value="org.org_id">{{ org.org_name }}</option>
                            </select>
                            </div>
                        </div>
                    </div>
                </div>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" @click="goBack" :disabled="confirmModal"> Back to Sessions </button>
                <button type="submit" class="btn btn-danger" style="margin-right:0.5rem" @click="deleteButtonClicked=true" :disabled="confirmModal">Delete</button>
                <button type="submit" class="btn btn-primary"  @click="updateButtonClicked = true" :disabled="confirmModal">Update </button>
            </div>
        </form>
    </div>
    </main>

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>
    </div>
</template>

<script>
import axios from "axios";
import ConfirmModal from './ConfirmModal.vue'
import LoadingModal from './LoadingModal.vue'
import { getSpecificSessionAPI, getEventsAPI, getOrgsAPI, updateSessionAPI, deleteSessionAPI } from '../api/api.js'
export default {
    name: 'SessionsUpdate',
    components: {
        ConfirmModal,
        LoadingModal
    },
    data() {
        return {
            session_info: {
                session_id: this.$route.params.session_id,
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
            temp_time_in: null,
            isLoading: false,
            confirmModal: false,
            title: '',
            message: '',
            errors: {},
            submitPressed: false,
            closedSession: false,
        };
    },
    watch: {
        'session_info.session_date'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('date')
                } else {
                    this.addValidationStyle('date', 'Date is required.')
                }
            }
        },
        'session_info.time_in'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('timeIn')
                } else {
                    this.addValidationStyle('timeIn', 'Check in time is required.')
                }
            }
        },
        'session_info.event_id'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('event')
                } else {
                    this.addValidationStyle('event', 'Event is required.')
                }
            }
        },
    },
    mounted() {
        this.loadData();
    },
    methods: {
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        async loadData() {
            console.log('data started to load')
            this.isLoading = true;
            try {
                await this.getSession();
                await this.getEvents();
                await this.getOrgs();
            } catch (error) {
                console.log(error)
            }
            this.isLoading = false;
        },
        async getSession() {
            console.log('getSession started')
            console.log('this.session_info.session_id', this.session_info.session_id)
            try {
                const response = await getSpecificSessionAPI(this.session_info.session_id);
                    console.log('response:', response.data);
                    this.session_info.session_id = response.data[0].session_id;
                    this.session_info.time_in = response.data[0].time_in;
                    console.log('response.data[0].time_in:', response.data[0].time_in)
                    this.session_info.time_out = response.data[0].time_out;
                    if (this.session_info.time_out) {
                        console.log('closed session is true this.session_info.time_out:', this.session_info.time_out)
                        this.closedSession = true;
                    }
                    this.session_info.session_date = response.data[0].session_date;
                    //response.data[0].session_date;
                    this.session_info.session_comment = response.data[0].session_comment;
                    this.session_info.full_name = response.data[0].full_name;
                    this.session_info.org_id = response.data[0].org_id;
                    this.session_info.event_id = response.data[0].event_id;
                    //format datetime
                    const timeParts = this.session_info.time_in.split(':');
                    const hours = parseInt(timeParts[0]);
                    const minutes = parseInt(timeParts[1]);
                    const time = new Date();
                    time.setHours(hours);
                    time.setMinutes(minutes);
                    const options = { hour12: true, hour: 'numeric', minute: 'numeric' };
                    this.temp_time_in = time.toLocaleTimeString(navigator.language, options);
                    console.log('temp_time_in', this.temp_time_in)

            } catch (error) {
                console.log(error)
            }
        },
        async getEvents() {
            try {
                const response = await getEventsAPI();
                // iterate through JSON response and add orgs to orgs array
                for (var i = 0; i < response.data.length; i++) {
                    this.events.push({
                        event_name: response.data[i].event_name,
                        event_id: response.data[i].event_id
                    });
                }
            } catch (error) {
                console.log(error)
            }
        },
        async getOrgs() {
            try {
                const response = await getOrgsAPI();
                for (var i = 0; i < response.data.length; i++) {
                    this.orgs.push({
                        org_name: response.data[i].org_name,
                        org_id: response.data[i].org_id
                    });
                }

            } catch (error) {
                console.log(error)
            }
        },
        submitForm() {
            this.submitPressed = true

            this.errors = {}

            if (!this.session_info.session_date) {
                this.errors.date = 'Session date is required.'
            }
            if (!this.session_info.time_in) {
                this.errors.timeIn = 'Check in time is required.'
            }
            if (!this.session_info.event_id) {
                this.errors.event = 'Event is required.'
            }
            if (this.closedSession) {
                if (!this.session_info.time_out) {
                    this.errors.closedSession = 'This session is closed. Check out time is required.'
                }
            }
            if (this.session_info.time_out) {
                // Compare time_in and time_out
                const timeInMs = Date.parse(`2000-01-01 ${this.session_info.time_in}`);
                const timeOutMs = Date.parse(`2000-01-01 ${this.session_info.time_out}`);

                if (timeOutMs < timeInMs) {
                    this.errors.timeError = 'Time out must not be earlier than time in.';
                }
            }
            if (Object.keys(this.errors).length === 0) {
                if (this.updateButtonClicked == true){
                    this.updateButtonClicked = false
                    console.log('this.session.org_id', this.session_info.org_id)
                    this.confirmModal = true
                    this.title = 'Please Confirm Update'
                    this.message = "Are you sure you want to update this session?"
                }
                else if (this.deleteButtonClicked = true){
                    this.deleteButtonClicked = false
                    this.confirmModal = true
                    this.title = 'Please Confirm Delete'
                    this.message = "Are you sure you want to delete this session?"
                }
            }
        },
        async updateSession() {
            try {
                await updateSessionAPI(this.session_info);
                    this.session_info={}
                    if (this.closedSession) {
                        this.$router.push('/admin/closed_sessions?update=true')
                    } else {
                        this.$router.push('/admin/sessions_list?update=true')
                    }
            } catch (error) {
                console.log(error)
            }
        },
        async deleteSession() {
            try {
                await deleteSessionAPI(this.session_info)
                    this.session_info = {}
                    if (this.closedSession) {
                        this.$router.push('/admin/closed_sessions?delete=true')
                    } else {
                        this.$router.push('/admin/sessions_list?delete=true')
                    }
            } catch (error) {
                console.log(error)
            }
        },
        goBack() {
            this.$router.go(-1)
        },
        closeConfirmModal(value) {
            this.confirmModal = false
            if (value === 'yes') {
                if (this.title === 'Please Confirm Update') {
                    this.title = '';
                    this.message = '';
                    this.updateSession();
                } else if (this.title === 'Please Confirm Delete') {
                    this.title = '';
                    this.message = '';
                    this.deleteSession();
                }
            }
        },
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
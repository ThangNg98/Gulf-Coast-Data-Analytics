<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container" style="text-align:left"> 
        <form @submit.prevent="submitForm">
            <div class="text-danger" style="margin-top: 1rem; font-weight: bold">
                * Required
            </div>
            <div class="">
                <label for="eventName" class="form-label">Event Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" ref="eventName" v-model="this.events.event_name" :class="{ 'is-invalid': errors.eventName }" :maxlength="100" :disabled="confirmModal">
                <div class="invalid-feedback">{{errors.eventName}}</div>

                <label for="eventDescription" class="form-label"> Description</label>
                <textarea class="form-control" ref="eventDescription" v-model="this.events.event_description" :disabled="confirmModal"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" :disabled="confirmModal"> <router-link class="nav-link" to="/admin/events"> Back to Events</router-link></button>
                <button type="submit" class="btn btn-danger" style="margin-right:0.5rem" @click="deleteButtonClicked = true" :disabled="confirmModal">Delete</button>
                <button type="submit" class="btn btn-primary" @click="updateButtonClicked = true" :disabled="confirmModal">Update</button>
                
            </div>
        </form>
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Total Hours</th>
                        <th scope="col">Number of Volunteers</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td v-if="hours != null"> {{ this.hours }}</td>
                            <td v-else> 0 </td>
                            <td v-if="num_volunteers != 0"> {{ this.num_volunteers }}</td>
                            <td v-else> 0 </td>
                        </tr>
                    </tbody>
                </table>
        </div>
        
    </div>

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

    </main>
</template>

<script>
import axios from "axios";
import ConfirmModal from './ConfirmModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { getEventAPI, updateEventAPI, deleteEventAPI } from '../api/api.js'
export default {
    name: 'EventsUpdate',
    components: {
        ConfirmModal,
        LoadingModal,
    },
    data() {
        return {
            msg : "Update Event",
            events: {
                event_id: '',
                event_name: '',
                event_description: ''
            },
            updateButtonClicked: false,
            deleteButtonClicked: false,
            hours: null,
            num_volunteers: 0,
            errors: {},
            submitPressed: false,
            confirmModal: false,
            isLoading: false
        };
    },
    watch: {
        'events.event_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('eventName')
                } else {
                    this.addValidationStyle('eventName', 'Organization name is required.')
                }
            }
        },
    },
    created() {
        this.loadData();
    },
    methods: {
        async loadData() {
            this.isLoading = true;
            try {
                const response = await getEventAPI(this.$route.params.event_id);
                this.events.event_id = response.data[0].event_id;
                this.events.event_name = response.data[0].event_name;
                this.events.event_description = response.data[0].event_description;
                this.hours = response.data[0].total_hours;
                this.num_volunteers = response.data[0].num_volunteers;
            } catch (error) {
                console.log(error)
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
            console.log(value)
            if (value === 'yes') {
                if (this.title === 'Please Confirm Update') {
                    console.log('update confirm')
                    this.title = '';
                    this.message = '';
                    this.updateEvent();

                }
                else if (this.title === 'Please Confirm Delete') {
                    console.log('delete confirm')
                    this.title = '';
                    this.message = '';
                    this.deleteEvent();
                }
            }
        },
        async updateEvent() {
            try {
                await updateEventAPI(this.events);
                this.events={}
                this.$router.push('/admin/events?update=true')
            } catch (error) {
                console.log(error)
            }
        },
        async deleteEvent() {
            try {
                await deleteEventAPI(this.events);
                this.events={}
                this.$router.push('/admin/events?delete=true')
            } catch (error) {
                console.log(error)
            }
        },
        submitForm() {

            this.submitPressed = true

            this.errors = {}

            if (!this.events.event_name) {
                this.errors.eventName = 'Event name is required.'
            }

            if (Object.keys(this.errors).length === 0) {
                if (this.updateButtonClicked == true) {
                    console.log('update clicked')
                    this.updateButtonClicked = false
                    this.confirmModal = true
                    this.title = 'Please Confirm Update'
                    this.message = "Are you sure you want to update this event?"
                }
                else if (this.deleteButtonClicked == true) {
                    console.log('delete clicked')
                    this.deleteButtonClicked = false
                    this.confirmModal = true
                    this.title = 'Please Confirm Delete'
                    this.message = "Are you sure you want to delete this event?"
                }
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
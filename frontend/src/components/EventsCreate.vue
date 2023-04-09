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
            <div>
                <label for="eventName" class="form-label">Event Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control" ref="eventName" v-model="event_info.event_name" :class="{ 'is-invalid': errors.eventName }" :maxlength="100" :disabled="confirmModal">
                <div class="invalid-feedback">{{errors.eventName}}</div>

                <label for="eventDescription" class="form-label"> Description</label>
                <textarea class="form-control" ref="eventDescription" v-model="event_info.event_description" :disabled="confirmModal"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" :disabled="confirmModal"> <router-link class="nav-link" to="/admin/events"> Back to Events</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" :disabled="confirmModal">Submit</button>
          </div>
        </form>
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
import { createEventAPI } from '../api/api.js'
export default {
    name: 'EventsCreate',
    components: {
        ConfirmModal,
        LoadingModal,
    },
    data() {
        return {
            msg : "Create New Event",
            event_info : {
                event_name: '',
                event_description: ''
            },
            confirmModal: false,
            title: '',
            message: '',
            errors: {},
            submitPressed: false,
            isLoading: false,
        };
    },
    watch: {
        'event_info.event_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('eventName')
                } else {
                    this.addValidationStyle('eventName', 'Organization name is required.')
                }
            }
        },
    },
    methods: {
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        closeConfirmModal(value) {
            this.confirmModal = false
            this.title = ''
            this.message = ''
            console.log(value)
            if (value === 'yes') {
                this.createEvent();
            }
        },
        async createEvent() {
            try {
                await createEventAPI(this.event_info);
                this.event_info={}
                this.$router.push('/admin/events?success=true')
            } catch(error) {
                console.log(error)
            }
        },
        submitForm() {
            this.submitPressed = true
            this.errors = {}
            if (!this.event_info.event_name) {
                this.errors.eventName = 'Event name is required.'
            }
            if (Object.keys(this.errors).length === 0) {
                this.confirmModal = true
                this.title = 'Please Confirm Creation'
                this.message = 'Are you sure you want to create this event?'
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
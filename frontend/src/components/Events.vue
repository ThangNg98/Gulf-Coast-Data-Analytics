<template>
    <main>
      <div class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-6">
      <div class="row">
        <div class="col-12 text-center mb-3">
          <h1>{{ msg }}</h1>
        </div>
        <div class="col-12 mb-3">
          <div class="text-start">
            <h4>Search Event By</h4>
          </div>
          <select
            class="form-select"
            v-model="searchBy"
          >
            <option value="Event Name">Event Name</option>
            <option value="Event Description">Event Description</option>
          </select>
        </div>
        <div v-if="searchBy === 'Event Name'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="name"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter event name"
          />
        </div>
        <div v-if="searchBy === 'Event Description'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="desc"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter event description"
          />
        </div>
        <div class="col-12 d-flex justify-content-end gap-2">
          <button
            class="btn btn-outline-secondary"
            @click="clearSearch"
            type="submit"
          >
            Clear Search
          </button>
          <button
            class="btn btn-primary"
            @click="handleSubmitForm"
            type="submit"
          >
            Search Events
          </button>
        </div>
      </div>
    </div>
  </div>
</div>



    <div class="container1 table-wrapper"> 
        <div class="table-responsive-md">
            <table class="table table-bordered text-start" style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col" style="width: 30%;">Event Name</th>
                        <th scope="col" style="width: 70%;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                        @click="editEvent(event.event_id)"
                        :key="event.event_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === event.event_id }"
                        @mouseenter="hoverId = event.event_id"
                        @mouseleave="hoverId = null"
                        v-for="event in eventsFiltered" >
                            <td style="text-align:left">{{ event.event_name }}</td>
                            <td style="text-align:left">{{ event.event_description }}</td>
                        </tr>
                    </tbody>
                </table>
        </div>
    </div>
    <div style="margin-top: 2rem;margin-left: 30%">
            <router-link class="nav-link" to="/admin/create_event"> <button type="submit" class="btn btn-success" style="margin-right:0.5rem" >Create New Event</button> </router-link>
    </div>

    <Transition name="bounce">
        <SuccessModal v-if="successModal" @close="closeSuccessModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <DeleteModal v-if="deleteModal" @close="closeDeleteModal" :title="title" :message="message" />
    </Transition>

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>
    
    </main>
</template>

<script>
import axios from "axios";
import SuccessModal from './SuccessModal.vue'
import UpdateModal from './UpdateModal.vue'
import DeleteModal from './DeleteModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { getEventsAPI } from '../api/api.js'
export default {
    name: 'Events',
    components: {
        SuccessModal,
        UpdateModal,
        DeleteModal,
        LoadingModal,
    },
    data() {
        return {
            msg : "List of Events",
            events: [],
            hoverId: null,
            successModal: false,
            updateModal: false,
            deleteModal: false,
            searchBy: '',
            name: '',
            desc: '',
            eventsFiltered: [],
            isLoading: false,
            isMounted: false,
        }
    },
    updated() {
        if (!this.isMounted) {
            console.log('pseudo mount')
            const query = new URLSearchParams(this.$route.query);
            if (query.get('success') === 'true') {
                console.log('success is true')
                this.successModal = true;
                this.title = "Success!"
                this.message = "Event successfully created."
            }
            if (query.get('update') === 'true') {
                console.log('update is true')
                this.updateModal = true;
                this.title = "Updated!"
                this.message = "Event successfully updated."
            }
            if (query.get('delete') === 'true') {
                console.log('delete is true')
                this.deleteModal = true;
                this.title = "Deleted!"
                this.message = "Event successfully deleted."
            }
            this.isMounted = true
        }
    },
    mounted() {
        this.loadData();
    },
    methods: {
      async loadData() {
        this.isLoading = true;
        try {
          const response = await getEventsAPI();
          // iterate through JSON response and add events to events array
          for (var i = 0; i < response.data.length; i++) {
              this.events.push(response.data[i]);
          }
          this.setEventsList();
        } catch (error) {
          console.log(error)
        }
        this.isLoading = false;
      },
        closeSuccessModal() {
            this.successModal = false;
            this.title = '';
            this.message = '';
        },
        closeUpdateModal() {
            this.updateModal = false;
            this.title = '';
            this.message = '';
        },
        closeDeleteModal() {
            this.deleteModal = false;
            this.title = '';
            this.message = '';
        },
        setEventsList() {
            this.eventsFiltered = this.events
        },
        editEvent(event_id) {
            this.$router.push({ name: 'EventsUpdate', params: 
            { event_id: event_id } });
        },
        handleSubmitForm() {
        //if user searched by event name
            if (this.searchBy === 'Event Name') {
            //filter the events list by event name
                this.eventsFiltered = this.events.filter((event) => event.event_name.toLowerCase().includes(this.name.toLowerCase()));
            } 
            //if user searched by event description
            else if (this.searchBy === 'Event Description') {
                //filter the events list by event description
                this.eventsFiltered = this.events.filter((event) => event.event_description.toLowerCase().includes(this.desc.toLowerCase()));
            }
        },
        //method called when user clicks "Clear Search" button
        clearSearch() {
            // Resets all the variables
            this.searchBy = ''
            this.name = ''
            this.desc = ''
            this.setEventsList()
        },
    },
}
</script>

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}
.table td {
    word-wrap: break-word;
    min-width: 120px;
    max-width: 160px;
}

.hoverRow {
    background-color: rgba(230, 231, 235, 1);
    transition: background-color 0.3s ease-in-out;
  }

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}

.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}
</style>
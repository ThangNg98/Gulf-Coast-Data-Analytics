<template>
    <main>
    <div>
        <h2 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> <router-link  class="text-decoration-none" to="/admin/sessions_list">{{ msg }}</router-link> | <router-link  class="text-decoration-none" to="/admin/closed_sessions">{{ msg2 }}</router-link> </h2>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> Open Sessions</h1>

    </div>

    <div class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-6">
      <div class="row">
        <div class="col-12 text-center mb-3">
            <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> Open Sessions</h1>
        </div>
        <div class="col-12 mb-3">
          <div class="text-start">
            <h4>Search Session By</h4>
          </div>
          <select
            class="form-select"
            v-model="searchBy"
          >
            <option value="Volunteer Name">Volunteer Name</option>
            <option value="Volunteer Number">Volunteer Phone Number</option>
            <option value="Session Date">Session Date</option>
          </select>
        </div>
        <div v-if="searchBy === 'Volunteer Name'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="volunteerName"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter volunteer's name"
          />
        </div>
        <div v-if="searchBy === 'Volunteer Number'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="formattedPhone"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter volunteer's phone number"
            maxlength="14"
          />
        </div>
        <div class="col-12 mb-3" v-if="searchBy === 'Session Date'">
          <input class="form-control" type="date" name="sessionDate" ref="sessionDate" v-model="sessionDate">
          <div class="text-start">
          </div>
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
            Search Sessions
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

    <div class="container">     
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: left; max-width: 50%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy ='volunteer_name'" scope="col">Volunteer Name</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='session_date'" scope="col">Session Date</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='event_name'" scope="col">Event</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='org_name'" scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        <th scope="col">Session Comments</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="session in sortedItems" 
                            :key="session.session_id"
                            @click="editSessions(session.session_id)" 
                            :style="{ cursor: 'pointer' }"
                            :class="{ 'hoverRow': hoverId === session.session_id }"
                            @mouseenter="hoverId = session.session_id"
                            @mouseleave="hoverId = null"
                        >
                            <td>{{ session.volunteer_name }}</td>
                            <td>{{ session.session_date }}</td>
                            <td>{{ session.event_name }}</td>
                            <td>{{ session.org_name }}</td>
                            <td>{{ session.time_in }}</td>
                            <td>{{ session.session_comment }}</td>
                        </tr>
                    </tbody>
                </table>
        </div>

    </div>
    </main>

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <DeleteModal v-if="deleteModal" @close="closeDeleteModal" :title="title" :message="message" />
    </Transition>

</template>

<script>
import axios from "axios";
import LoadingModal from './LoadingModal.vue'
import UpdateModal from './UpdateModal.vue'
import DeleteModal from './DeleteModal.vue'
import { getSessionAPI } from '../api/api.js'
export default {
    name: 'SessionsList',
    components: {
        LoadingModal,
        UpdateModal,
        DeleteModal,
    },
    data() {
        return {
            msg : "Open",
            msg2 : "Closed",
            sessions:[],
            hoverId: null,
            sortBy: 'volunteer_name',
            sortDesc: false,
            isLoading: false,
            updateModal: false,
            deleteModal: false,
            sessionsFiltered: [],
            searchBy: null,
            volunteerName: null,
            phone: null,
            sessionDate: null, 
        };
    },
    computed: {
        formattedPhone: {
            get() {
            if (!this.phone) return '';
            return this.formatPhoneNumber(this.phone);
            },
            set(value) {
            this.phone = value.replace(/[^\d]/g, '');
            },
        },
        formattedSessionDate() {
            if (!this.sessionDate) return '';

            const [year, month, day] = this.sessionDate.split('-');
            const date = new Date(year, month - 1, Number(day)); // Add 1 to the day

            const formattedDay = String(date.getDate()).padStart(2, '0');
            const formattedMonth = String(date.getMonth() + 1).padStart(2, '0');
            const formattedYear = date.getFullYear();

            return `${formattedMonth}/${formattedDay}/${formattedYear}`;
        },
        sortedItems() {
            const field = this.sortBy;
            const order = this.sortDesc ? -1 : 1;

            // Make a copy of the original array to avoid modifying the original data
            const sessions = this.sessionsFiltered.slice();

            // Custom sorting function
            const customSort = (a, b) => {
            // Check if the field is one of the fields that require alphabetical ordering
            if (['volunteer_name', 'event_name', 'org_name'].includes(field)) {
                const aValue = a[field].toLowerCase();
                const bValue = b[field].toLowerCase();

                if (aValue < bValue) return -1 * order;
                if (aValue > bValue) return 1 * order;
                return 0;
            }
            // Check if the field is 'session_date'
            else if (field === 'session_date') {
                const aValue = Date.parse(a[field]);
                const bValue = Date.parse(b[field]);
                const dateOrder = -1 * order;

                if (aValue < bValue) return -1 * dateOrder;
                if (aValue > bValue) return 1 * dateOrder;
                return 0;
            } else {
                if (a[field] < b[field]) return -1 * order;
                if (a[field] > b[field]) return 1 * order;
                return 0;
            }
            };



            // Sort the array by the specified field and order using the custom sorting function
            sessions.sort(customSort);

            return sessions;
        },
        },
        mounted() {
            this.loadData();
            const query = new URLSearchParams(this.$route.query);
            if (query.get('update') === 'true') {
                console.log('update is true')
                this.updateModal = true;
                this.title = "Updated!"
                this.message = "Session successfully updated."
            }
            if (query.get('delete') === 'true') {
                console.log('delete is true')
                this.deleteModal = true;
                this.title = "Deleted!"
                this.message = "Session successfully deleted."
            }
        },
    methods: {
        async loadData() {
            this.isLoading = true;
            try {
                const response = await getSessionAPI();
                for (var i = 0; i < response.data.length; i++) {
                    this.sessions.push(response.data[i]);
                }
                this.setSessionsList();
            } catch (error) {
                console.log(error)
            }
            this.isLoading = false;
        },
        setSessionsList() {
            this.sessionsFiltered = this.sessions
        },
        editSessions(session_id) {
            this.$router.push({ name: 'SessionsUpdate', params: 
            { session_id: session_id } });
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
        formatPhoneNumber(value) {
            const number = value.replace(/[^\d]/g, '');
            const len = number.length;

            if (len < 4) {
            return `(${number}`;
            } else if (len < 7) {
            return `(${number.slice(0, 3)}) ${number.slice(3)}`;
            } else {
            return `(${number.slice(0, 3)}) ${number.slice(3, 6)}-${number.slice(6)}`;
            }
        },
        handleSubmitForm() {
        //if user searches by Volunteer name
            if (this.searchBy === 'Volunteer Name') {
                this.sessionsFiltered = this.sessions.filter((session) => session.volunteer_name.toLowerCase().includes(this.volunteerName.toLowerCase()));
            
            } else if (this.searchBy === 'Volunteer Number') {
            //filter the client list by phone number
                this.sessionsFiltered = this.sessions.filter((session) => session.phone.includes(this.phone));
            } else if (this.searchBy === 'Session Date') {
                this.sessionsFiltered = this.sessions.filter(
                    (session) => session.session_date === this.formattedSessionDate
                );
            };
        },
        //method called when user clicks "Clear Search" button
        clearSearch() {
            // Resets all the variables
            this.searchBy = null
            this.volunteerName = null
            this.phone = null
            this.sessionDate = null
            this.setSessionsList();
        },
    },
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}
.table td {
    word-wrap: break-word;
    min-width: 160px;
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
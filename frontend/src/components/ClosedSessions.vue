<template>
    <main>
    <div>
        <h2 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> <router-link class="" to="/admin/sessions_list">{{ msg }}</router-link> | <router-link class="" to="/admin/closed_sessions">{{ msg2 }}</router-link> </h2>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> Closed Sessions </h1>
    </div>
    <div class="container"> 
        
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 20%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy ='volunteer_name'" scope="col">Volunteer Name</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='session_date'" scope="col">Session Date</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='event_name'" scope="col">Event</th>
                        <th :style="{ cursor: 'pointer' }" @click="sortBy='org_name'" scope="col">Organization</th>
                        <th scope="col">Time In</th>
                        <th scope="col">Time Out</th>
                        <th scope="col">Total Hours</th>
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
                            <td>{{ session.time_out }}</td>
                            <td>{{ session.total_hours }}</td>
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
import { getClosedSessionsAPI } from '../api/api.js'
export default {
    name: 'ClosedSessions',
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
            sortBy: 'session_date',
            sortDesc: false,
            isLoading: false,
            updateModal: false,
            deleteModal: false,
        };
    },
    computed: {
        sortedItems() {
            const field = this.sortBy;
            const order = this.sortDesc ? -1 : 1;

            // Make a copy of the original array to avoid modifying the original data
            const sessions = [...this.sessions];

            // Custom sorting function
            const customSort = (a, b) => {
            // Check if the field is one of the fields that require alphabetical ordering
            if (['volunteer_name', 'event_name', 'org_name'].includes(field)) {
                const aValue = a[field] === null ? '\uffff' : a[field].toLowerCase();
                const bValue = b[field] === null ? '\uffff' : b[field].toLowerCase();

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
                const response = await getClosedSessionsAPI();
                for (var i = 0; i < response.data.length; i++) {
                    this.sessions.push(response.data[i]);
                }
            } catch (error) {
                console.log(error)
            }
            this.isLoading = false;
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
    },
}
</script>

<style scoped>
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

.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 100%;
}

.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}
</style>
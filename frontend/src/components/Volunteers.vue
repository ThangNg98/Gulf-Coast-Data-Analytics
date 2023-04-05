<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container1"> 
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col">Volunteer Name</th>
                        <th style="width:5%" scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="volunteer in volunteers"
                        @click="editVolunteers(volunteer.volunteer_id)"
                        :key="volunteer.volunteer_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === volunteer.volunteer_id}"
                        @mouseenter="hoverId = volunteer.volunteer_id"
                        @mouseleave="hoverId = null"
                        
                        >
                            <td style="text-align:left">{{ volunteer.first_name }} {{ volunteer.last_name }}</td>
                            <!-- This v-if statement needs to check if the value is null and if it is display a 0 if it isnt then display the value-->
                            <td v-if="volunteer.total_hours == null">0</td>
                            <td v-else>{{ volunteer.total_hours }}</td>
                        </tr>
                    </tbody>
                </table>
        </div>
    </div>

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <DeleteModal v-if="deleteModal" @close="closeDeleteModal" :title="title" :message="message" />
    </Transition>


    </main>
</template>

<script>
import axios from "axios";
import UpdateModal from './UpdateModal.vue'
import DeleteModal from './DeleteModal.vue'
export default {
    name: 'Volunteers',
    components: {
        UpdateModal,
        DeleteModal
    },
    data() {
        return {
            msg : "List of Volunteers",
            volunteers: [],
            hoverId: null,
            updateModal: false,
            deleteModal: false,
            title: '',
            message: '',
            isMounted: false

        };
    },
    updated() {
        if (!this.isMounted) {
            console.log('pseudo mount')
            const query = new URLSearchParams(this.$route.query);
            if (query.get('update') === 'true') {
                console.log('update is true')
                this.updateModal = true;
                this.title = "Updated!"
                this.message = "Volunteer successfully updated."
            }
            if (query.get('delete') === 'true') {
                console.log('delete is true')
                this.deleteModal = true;
                this.title = "Deleted!"
                this.message = "Volunteer successfully deleted."
            }
            this.isMounted = true
        }
    },
    methods: {
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
        getVolunteers() {
            axios.get('http://127.0.0.1:5000/read_volunteers')
            .then(response => {
                // iterate through JSON response and add volunteers to the volunteer array
                for (var i = 0; i < response.data.length; i++) {
                    this.volunteers.push(response.data[i]);
                }
            })
            .catch(error => {
                console.log(error);
            });
        },
        editVolunteers(volunteer_id) {
            this.$router.push({ name: 'VolunteersUpdate', params: { volunteer_id: volunteer_id } });
        } 
    },
    mounted() {
        this.getVolunteers();
    }
}
</script>

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
}
.table td {
    word-wrap: break-word;
    min-width: 160px;
    max-width: 160px;
}
.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}

.hoverRow {
    background-color: rgba(230, 231, 235, 1);
    transition: background-color 0.3s ease-in-out;
  }
.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}
</style>
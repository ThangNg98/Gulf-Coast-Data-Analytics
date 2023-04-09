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
            <h4>Search Volunteer By</h4>
          </div>
          <select
            class="form-select"
            v-model="searchBy"
          >
            <option value="Volunteer Name">Volunteer Name</option>
            <option value="Volunteer Number">Volunteer Phone Number</option>
            <option value="Waiver Signed">Waiver Signed</option>
          </select>
        </div>
        <div v-if="searchBy === 'Volunteer Name'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="firstName"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter volunteer's first name"
          />
        </div>
        <div v-if="searchBy === 'Volunteer Name'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="lastName"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter volunteer's last name"
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
        <div class="form-check" v-if="searchBy === 'Waiver Signed'">
          <input class="form-check-input" type="radio" name="waiverSigned" id="signed" v-model="waiverSigned" value="true">
          <div class="text-start">
            <label class="form-check-label" for="signed">
              Volunteers who have signed the waiver.
            </label>
          </div>
        </div>
        <div class="form-check" v-if="searchBy === 'Waiver Signed'">
          <input class="form-check-input" type="radio" name="waiverSigned" id="not-signed" v-model="waiverSigned" value="false">
          <div class="text-start">
            <label class="form-check-label" for="not-signed">
              Volunteers who have not signed the waiver.
            </label>
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
            Search Volunteers
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

    <div class="container1"> 
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col">Volunteer Name</th>
                        <th style="width:5%" scope="col">Phone Number</th>
                        <th style="width:5%" scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="volunteer in volunteersFiltered"
                        @click="editVolunteers(volunteer.volunteer_id)"
                        :key="volunteer.volunteer_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === volunteer.volunteer_id}"
                        @mouseenter="hoverId = volunteer.volunteer_id"
                        @mouseleave="hoverId = null"
                        
                        >
                            <td style="text-align:left">{{ volunteer.first_name }} {{ volunteer.last_name }}</td>
                            <td style="text-align:left">{{ formatPhone(volunteer.phone) }}</td>
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

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

    </main>
</template>

<script>
import axios from "axios";
import UpdateModal from './UpdateModal.vue'
import DeleteModal from './DeleteModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { getVolunteersAPI } from '../api/api.js'
export default {
    name: 'Volunteers',
    components: {
        UpdateModal,
        DeleteModal,
        LoadingModal,
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
            isMounted: false,
            searchBy: '',
            firstName: '',
            lastName: '',
            phone: '',
            waiverSigned: false,
            volunteersFiltered: [],
            isLoading: false

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
    },
    mounted() {
        this.loadData();
    },
    methods: {
      async loadData() {
        this.isLoading = true;
        try {
          const response = await getVolunteersAPI();
          // iterate through JSON response and add volunteers to the volunteer array
          for (var i = 0; i < response.data.length; i++) {
              this.volunteers.push(response.data[i]);
          }
          this.setVolunteersList();
        } catch (error) {
          console.log(error)
        };
        this.isLoading = false;
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
        setVolunteersList() {
            this.volunteersFiltered = this.volunteers
        },
        editVolunteers(volunteer_id) {
            this.$router.push({ name: 'VolunteersUpdate', params: { volunteer_id: volunteer_id } });
        },
        //method called when user searches by Volunteer name or number
        handleSubmitForm() {
        //if user searches by Volunteer name
            if (this.searchBy === 'Volunteer Name') {
            //if user searches by both first name and last name
                if (this.firstName && this.lastName) {
                //filter the Volunteer list by first and last name
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.first_name.toLowerCase().includes(this.firstName.toLowerCase()) && volunteer.last_name.toLowerCase().includes(this.lastName.toLowerCase()));
                } 
                //if user searches only by first name
                else if (this.firstName && !this.lastName) {
                //filter the Volunteer list by first name only
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.first_name.toLowerCase().includes(this.firstName.toLowerCase()));
                } 
                //if user searches only by last name
                else if (this.lastName && !this.firstName) {
                //filter the volunteer list by last name only
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.last_name.toLowerCase().includes(this.lastName.toLowerCase()));
                }
            //if user searches by client phone number
            } else if (this.searchBy === 'Volunteer Number') {
            //filter the client list by phone number
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.phone.includes(this.phone));
            } else if (this.searchBy === 'Waiver Signed') {
              console.log('waiver signed button pressed')
              if (this.waiverSigned) {
                console.log('waiverSigned selected')
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.waiver_signed === 1)
                this.waiverSigned = false;
              } else if (!this.waiverSigned) {
                console.log('not waiverSigned selected')
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.waiver_signed === 2)
                this.waiverSigned = false;
              }
            };
        },
        //method called when user clicks "Clear Search" button
        clearSearch() {
        // Resets all the variables
        this.searchBy = ''
        this.name = ''
        this.phone = ''
        this.setVolunteersList()
        },
        formatPhone(phone) {
          const cleaned = ('' + phone).replace(/\D/g, '');
          const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
          if (match) {
            return '(' + match[1] + ') ' + match[2] + '-' + match[3];
          }
          return phone;
        },
    },
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

.form-check-label {
  margin-left: 1.5rem;
  font-weight: 400;
}

.form-check-input:checked ~ .form-check-label::before {
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.form-check-input:focus ~ .form-check-label::before {
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}
</style>
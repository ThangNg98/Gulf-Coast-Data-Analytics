<template>
    <main>

      <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
      <div class="px-10 pt-20">
        <div
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
        >
        <!--Search Volunteer By selection-->
          <h2 class="text-2xl font-bold">Search Volunteer By</h2>
          <!-- Displays Volunteer Name search field -->
          <div class="flex flex-col">
            <select
              class="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              v-model="searchBy"
            >
              <option value="Volunteer Name">Volunteer Name</option>
              <option value="Volunteer Number">Volunteer Number</option>
              <option value="Waiver Signed">Waiver Signed</option>
            </select>
          </div>
          <!--Input box for searching by Volunteer First Name-->
          <div class="flex flex-col" v-if="searchBy === 'Volunteer Name'">
            <label class="block">
              <input
                type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="firstName"
                v-on:keyup.enter="handleSubmitForm"
                placeholder="Enter first name"
              />
            </label>
          </div>
          <!--Input box for searching by Volunteer Last Name-->
          <div class="flex flex-col" v-if="searchBy === 'Volunteer Name'">
            <label class="block">
              <input
                type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="lastName"
                v-on:keyup.enter="handleSubmitForm"
                placeholder="Enter last name"
              />
            </label>
          </div>
          <!-- Displays Volunteer Number search field -->
          <div class="flex flex-col" v-if="searchBy === 'Volunteer Number'">
            <input
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              type="text"
              v-model="phone"
              v-on:keyup.enter="handleSubmitForm"
              placeholder="Enter Volunteer Phone Number"
            />
          </div>
          <div class="flex flex-col" v-if="searchBy === 'Waiver Signed'">
          <div>
            <label>
              <input type="radio" v-model="waiverSigned" value="true">
              Volunteers who have signed
            </label>
          </div>
          <div>
            <label>
              <input type="radio" v-model="waiverSigned" value="false">
              Volunteers who have not signed
            </label>
          </div>
        </div>
        </div>
        <div
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10"
        >
          <div></div>
          <div></div>
          <!--Clear Search button-->
          <div class="mt-5 grid-cols-2">
            <button
              class="mr-10 border border-red-700 bg-white text-red-700 rounded"
              @click="clearSearch"
              type="submit"
            >
              Clear Search
            </button>
            <!--Search Client button-->
            <button
              class="bg-red-700 text-white rounded"
              @click="handleSubmitForm"
              type="submit"
            >
              Search Client
            </button>
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

    <p>waiverSigned: {{ waiverSigned }}</p>


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
          this.setVolunteersList()
        } catch (error) {
          console.log(error)
        };
        this.isLoading = false;
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
            // axios.get('http://127.0.0.1:5000/read_volunteers')
            // .then(response => {
            //     // iterate through JSON response and add volunteers to the volunteer array
            //     for (var i = 0; i < response.data.length; i++) {
            //         this.volunteers.push(response.data[i]);
            //     }
            //     this.setVolunteersList()
            // })
            // .catch(error => {
            //     console.log(error);
            // });
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
              if (this.waiverSigned == true) {
                console.log('waiverSigned selected')
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.waiver_signed === 1)
              } else if (this.waiverSigned == false) {
                console.log('not waiverSigned selected')
                this.volunteersFiltered = this.volunteers.filter((volunteer) => volunteer.waiver_signed === 2)
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
</style>
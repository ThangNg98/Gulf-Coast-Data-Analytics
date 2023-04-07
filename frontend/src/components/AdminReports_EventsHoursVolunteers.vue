<template>
    <div class="container1"> 
          <div style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
              Events by Hours and Volunteers
          </div>
          <div style="margin:auto; text-align: left; max-width: 30%; margin-top: 2rem">
            Filter By:
            <select
              class="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              v-model="searchBy"
            >
              <option value="Total Hours">Total Hours</option>
              <option value="Number of Volunteers">Number of Volunteers</option>
            </select>
          </div>
          <div class="flex flex-col" v-if="searchBy === 'Total Hours'">
            <label class="block">
              <input
                type="number"
                v-model="total_hours"
                v-on:keyup.enter="handleFilter"
                placeholder="Enter number of hours"
              />
            </label>
          </div>
          
          <div class="flex flex-col" v-if="searchBy === 'Number of Volunteers'">
            <label class="block">
              <input
                type="number"
                v-model="number_of_volunteers"
                v-on:keyup.enter="handleFilter"
                placeholder="Enter number of volunteers"
              />
            </label>
          </div>

          <div class="mt-5 grid-cols-2">
            <!--Clear Search button-->
            <button
              @click="clearFilter"
            >
              Clear Filter
            </button>
            <!--Search Organization button-->
            <button
              @click="handleFilter"
            >
              Apply Filter
            </button>
          </div>

          <div class="table-responsive-md">
          <table class="table table-striped table-hover"  style="margin:auto; text-align: center; max-width: 50%; margin-top: 2rem">
              <thead class="theadsticky">
                  <tr>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='event_name'">Event</th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_event'">Total hours</th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='num_volunteers'">Number of Volunteers</th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="event in sortedItems" :key="event.event_id" style="text-align:left">
                      <td style="text-align:left"> {{ event.event_name }}</td>
                      <td style="text-align:left"> {{ event.total_hours_per_event }}</td>
                      <td style="text-align:left"> {{ event.num_volunteers }}</td>
                  </tr>

              </tbody>
              </table>
      </div>
    </div>

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getEventsHoursVolunteersAPI } from '../api/api.js'
export default {
  name: 'EventsHoursVolunteers',
  components: {
      LoadingModal,
  },
  data() {
      return {
          events: [],
          isLoading: false,
          sortBy: 'total_hours_per_event',
          sortDesc: false,
          searchBy: '',
          total_hours: null,
          number_of_volunteers: null,
          eventsFiltered: [],
      }
  },
  mounted() {
      this.loadData();
  },
  computed: {
    sortedItems() {
        const field = this.sortBy;
        let order = this.sortDesc ? -1 : 1;

        // If sorting by total hours, reverse the sort order to make higher hours come first
        if (field === 'num_volunteers' || field === 'total_hours_per_event') {
            order *= -1;
        }

        // Make a copy of the original array to avoid modifying the original data
        const events = this.eventsFiltered.slice();

        // Sort the array by the specified field and order
        events.sort((a, b) => {
            if (a[field] < b[field]) return -1 * order;
            if (a[field] > b[field]) return 1 * order;
            return 0;
        });

        return events;
    },
  },
  methods: {
      async loadData() {
          this.isLoading = true;
          try {
              const response = await getEventsHoursVolunteersAPI();
              this.events = response.data;
              console.log('events:', this.events)
              this.setEventsList();
          } catch (error) {
              console.log(error)
          }
          this.isLoading = false;
      },
      setEventsList() {
        console.log('setEventsList called')
            this.eventsFiltered = this.events
      },
      handleFilter() {
        console.log('filter handled')
        if (this.searchBy === 'Total Hours') {
            console.log('filter by total hours')
            this.eventsFiltered = this.events.filter((event) => {
                const totalHours = parseFloat(event.total_hours_per_event);
                return totalHours >= this.total_hours;
            });

            } 
            //if user searched by Organization address
            else if (this.searchBy === 'Number of Volunteers') {
                console.log('filter by num volunteers')
                //filter the Organizations list by Organization address
                this.eventsFiltered = this.events.filter((event) => {
                    const totalVolunteers = parseFloat(event.num_volunteers);
                    return totalVolunteers >= this.number_of_volunteers;
                });
            }
      },
      clearFilter() {
            // Resets all the variables
            this.searchBy = ''
            this.total_hours = ''
            this.number_of_volunteers = ''
            this.setEventsList()
        },
  },
}
</script>

<style>
.container1 {
margin: auto;
padding-left: auto;
padding-right: auto
}
</style>
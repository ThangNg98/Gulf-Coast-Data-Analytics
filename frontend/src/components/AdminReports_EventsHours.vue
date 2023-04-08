<template>
    <div class="container1"> 
          <div style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
              Events by Hours
          </div>
          <div style="margin:auto; text-align: left; max-width: 30%; margin-top: 2rem">
            Filter By Total Hours
          </div>
          <div class="flex flex-col">
            <label class="block">
              <input
                type="number"
                v-model="total_hours"
                v-on:keyup.enter="handleFilter"
                placeholder="Enter number of hours"
              />
            </label>
            <div class="mt-5 grid-cols-2">
                <!--Clear Search button-->
                <button
                @click="clearFilter"
                >
                Clear Filter
                </button>

                <button
                @click="handleFilter"
                >
                Apply Filter
                </button>
          </div>
          </div>
          <div class="table-responsive-md">
          <table class="table table-striped table-hover"  style="margin:auto; text-align: center; max-width: 50%; margin-top: 2rem">
              <thead class="theadsticky">
                  <tr>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='event_name'">
                    Event
                    <i class="bi bi-sort-alpha-down"></i>
                  </th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_event'">
                    Hours
                    <i class="bi bi-sort-numeric-down-alt"></i>
                  </th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="event in sortedItems" :key="event.event_id" style="text-align:left">
                      <td style="text-align:left"> {{ event.event_name }}</td>
                      <td style="text-align:left"> {{ event.total_hours_per_event }}</td>
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
import { getEventsHoursAPI } from '../api/api.js'
export default {
  name: 'EventsHours',
  components: {
      LoadingModal,
  },
  data() {
      return {
          events: [],
          isLoading: false,
          sortBy: 'event_hours',
          sortDesc: false,
          total_hours: null,
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
        if (field === 'total_hours_per_event') {
            order *= -1;
        }

        // Make a copy of the original array to avoid modifying the original data
        const events = this.eventsFiltered.slice();

        // Sort the array by the specified field and order
        events.sort((a, b) => {
        if (field === 'total_hours_per_event') {
            const aHours = parseFloat(a[field]);
            const bHours = parseFloat(b[field]);
            if (aHours < bHours) return -1 * order;
            if (aHours > bHours) return 1 * order;
        } else {
            if (a[field] && b[field]) {
            const aValue = a[field].toLowerCase();
            const bValue = b[field].toLowerCase();
            if (aValue < bValue) return -1 * order;
            if (aValue > bValue) return 1 * order;
            }
        }
        return 0;
        });

        return events;
    },
  },
  methods: {
      async loadData() {
        console.log('data loaded')
          this.isLoading = true;
          try {
              const response = await getEventsHoursAPI();
              this.events = response.data;
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
        console.log('filter by total hours')
        //filter the Organizations list by Organization address
        this.eventsFiltered = this.events.filter((event) => {
            const totalHours = parseFloat(event.total_hours_per_event);
            return totalHours >= this.total_hours;
        });
      },
      clearFilter() {
            // Resets all the variables
            this.total_hours = ''
            this.setEventsList();
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
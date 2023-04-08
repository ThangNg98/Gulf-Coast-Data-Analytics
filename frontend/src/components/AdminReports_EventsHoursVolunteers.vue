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
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='event_name'">
                    Event
                    <i class="bi bi-sort-alpha-down"></i>
                  </th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_event'">
                    Total hours
                    <i class="bi bi-sort-numeric-down-alt"></i>
                  </th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='num_volunteers'">
                    Number of Volunteers
                    <i class="bi bi-sort-numeric-down-alt"></i>
                  </th>
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

      <div class="chart-container">
        <canvas ref="chartCanvas"></canvas>
      </div>
    </div>

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getEventsHoursVolunteersAPI } from '../api/api.js'
import Chart from 'chart.js/auto';
import { shallowRef } from 'vue';
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
          chart: null,
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
        if (field === 'total_hours_per_event') {
            const aHours = parseFloat(a[field]);
            const bHours = parseFloat(b[field]);
            if (aHours < bHours) return -1 * order;
            if (aHours > bHours) return 1 * order;
        } else if (field === 'num_volunteers') {
            if (a[field] < b[field]) return -1 * order;
            if (a[field] > b[field]) return 1 * order;
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
    chartData() {
      return {
        labels: this.eventsFiltered.map((event) => event.event_name),
        datasets: [
          {
            label: 'Total Hours per Event',
            data: this.eventsFiltered.map((event) => parseFloat(event.total_hours_per_event)),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
          },
          {
            label: 'Number of Volunteers',
            data: this.eventsFiltered.map((event) => parseInt(event.num_volunteers)),
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1,
          },
        ],
      };
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
              this.createChart();
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
            this.updateChart();
      },
      clearFilter() {
            // Resets all the variables
            this.searchBy = ''
            this.total_hours = ''
            this.number_of_volunteers = ''
            this.setEventsList();
            this.updateChart();
      },
      createChart() {
        const ctx = this.$refs.chartCanvas.getContext('2d');
        this.chart = shallowRef(
          new Chart(ctx, {
          type: 'bar',
          data: this.chartData,
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        }));
      },
      updateChart() {
        this.chart.data.labels = this.chartData.labels;
        console.log('labels updated')
        this.chart.data.datasets = this.chartData.datasets;
        console.log('data updated')
        this.chart.update();
        console.log('chart updated')
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

.chart-container {
  position: relative;
  max-width: 100%;
  margin: 2rem auto;
  height: 40vh;
}
</style>
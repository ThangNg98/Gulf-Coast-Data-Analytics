<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-6">
      <div class="row">
        <div class="col-12 text-center mb-3">
          <h2>
            Events by Hours
            <small class="text-muted">Report</small>
          </h2>
        </div>
        <div class="col-12 mb-3">
          <div class="text-start">
            <label for="totalHours" class="form-label"><h5>Filter by Total Hours</h5></label>
          </div>
          <input
            type="number"
            class="form-control"
            id="totalHours"
            v-model="total_hours"
            v-on:keyup.enter="handleFilter"
            placeholder="Enter the minimum number of hours:"
          />
        </div>
        <div class="col-12 d-flex justify-content-end gap-2">
          <button
            class="btn btn-outline-secondary"
            @click="clearFilter"
          >
            Clear Filter
          </button>
          <button
            class="btn btn-primary"
            @click="handleFilter"
          >
            Apply Filter
          </button>
        </div>
      </div>
    </div>
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
                      <td style="text-align:left"> {{ event.total_hours_per_event}}</td>
                  </tr>

              </tbody>
              </table>
      </div>

      <div class="chart-container">
        <canvas ref="chartCanvas"></canvas>
      </div>
    

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getEventsHoursAPI } from '../api/api.js'
import Chart from 'chart.js/auto';
import { shallowRef } from 'vue';
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
    chartData() {
      return {
        labels: this.eventsFiltered.map((event) => event.event_name),
        datasets: [
          {
            label: 'Total Hours per Event',
            data: this.eventsFiltered.map((event) => parseFloat(event.total_hours_per_event)),
            backgroundColor: 'rgba(54, 162, 235, 0.4)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
          },
        ],
      };
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
        console.log('filter by total hours')
        this.eventsFiltered = this.events.filter((event) => {
            const totalHours = parseFloat(event.total_hours_per_event);
            return totalHours >= this.total_hours;
        });
        this.updateChart();
      },
      clearFilter() {
            // Resets all the variables
            this.total_hours = ''
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
            plugins: {
              legend: {
                display: false, // set the display property to false
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
.container {
margin: auto;
padding-left: auto;
padding-right: auto
}

.chart-container {
  position: relative;
  max-width: 70%;
  margin: 2rem auto;
  height: 40vh;
}
</style>
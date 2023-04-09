<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 col-md-6">
        <div class="row">
          <div class="col-12 text-center mb-3">
            <h2>
              Organizations by Volunteers
              <small class="text-muted">Report</small>
            </h2>
          </div>
          <div class="col-12 mb-3">
            <div class="text-start">
              <label for="totalHours" class="form-label"><h5>Filter by Number of Volunteers</h5></label>
            </div>
            <input
              type="number"
              class="form-control"
              id="totalHours"
              v-model="number_of_volunteers"
              v-on:keyup.enter="handleFilter"
              placeholder="Enter the minimum number of volunteers:"
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
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='org_name'">
                    Organization
                    <i class="bi bi-sort-alpha-down"></i>
                </th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='num_volunteers'">
                    Number of Volunteers
                    <i class="bi bi-sort-numeric-down-alt"></i>
                </th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="org in sortedItems" :key="org.org_id" style="text-align:left">
                      <td style="text-align:left"> {{ org.org_name }}</td>
                      <td style="text-align:left"> {{ org.num_volunteers }}</td>
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
import { getOrgsVolunteersAPI } from '../api/api.js'
import Chart from 'chart.js/auto';
import { shallowRef } from 'vue';
export default {
  name: 'OrgsVolunteers',
  components: {
      LoadingModal,
  },
  data() {
      return {
          orgs: [],
          isLoading: false,
          sortBy: 'num_volunteers',
          sortDesc: false,
          number_of_volunteers: null,
          orgsFiltered: [],
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
        if (field === 'num_volunteers') {
            order *= -1;
        }

        // Make a copy of the original array to avoid modifying the original data
        const orgs = this.orgsFiltered.slice();

        // Sort the array by the specified field and order
        orgs.sort((a, b) => {
        if (field === 'num_volunteers') {
            const aHours = a[field];
            const bHours = b[field];
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

        return orgs;
    },
    chartData() {
      return {
        labels: this.orgsFiltered.map((org) => org.org_name),
        datasets: [
          {
            label: 'Total Hours per Organization',
            data: this.orgsFiltered.map((org) => parseFloat(org.num_volunteers)),
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
          this.isLoading = true;
          try {
              const response = await getOrgsVolunteersAPI();
              this.orgs = response.data;
              console.log('data loaded')
              this.setOrgsList();
              this.createChart();
          } catch (error) {
              console.log(error)
          }
          this.isLoading = false;
      },
      setOrgsList() {
        console.log('setOrgsList called')
            this.orgsFiltered = this.orgs
      },
      handleFilter() {
        console.log('filter by num volunteers')
        //filter the Organizations list by Organization address
        this.orgsFiltered = this.orgs.filter((org) => {
            const totalVolunteers = parseFloat(org.num_volunteers);
            return totalVolunteers >= this.number_of_volunteers;
        });
        this.updateChart();
      },
      clearFilter() {
            // Resets all the variables
            this.number_of_volunteers = ''
            this.setOrgsList();
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
  max-width: 100%;
  margin: 2rem auto;
  height: 40vh;
}
</style>
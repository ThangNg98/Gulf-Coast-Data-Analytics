<template>
    <div class="container1"> 
          <div style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
              Organizations by Hours
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
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='org_name'">
                    Organization
                    <i class="bi bi-sort-alpha-down"></i>
                </th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_org'">
                    Hours
                    <i class="bi bi-sort-numeric-down-alt"></i>
                </th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="org in sortedItems" :key="org.org_id" style="text-align:left">
                      <td style="text-align:left"> {{ org.org_name }}</td>
                      <td style="text-align:left"> {{ org.total_hours_per_org }}</td>
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
import { getOrgsHoursAPI } from '../api/api.js'
import Chart from 'chart.js/auto';
import { shallowRef } from 'vue';
export default {
  name: 'OrgsHours',
  components: {
      LoadingModal,
  },
  data() {
      return {
          orgs: [],
          isLoading: false,
          sortBy: 'organization_hours',
          sortDesc: false,
          total_hours: null,
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
        if (field === 'total_hours_per_org') {
        order *= -1;
        }

        // Make a copy of the original array to avoid modifying the original data
        const orgs = this.orgsFiltered.slice();

        // Sort the array by the specified field and order
        orgs.sort((a, b) => {
        if (field === 'total_hours_per_org') {
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

        return orgs;
    },
    chartData() {
      return {
        labels: this.orgsFiltered.map((org) => org.org_name),
        datasets: [
          {
            label: 'Total Hours per Organization',
            data: this.orgsFiltered.map((org) => parseFloat(org.total_hours_per_org)),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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
              const response = await getOrgsHoursAPI();
              this.orgs = response.data;
              this.setOrgsList();
              this.createChart();
          } catch (error) {
              console.log(error)
          }
          this.isLoading = false;
      },
      setOrgsList() {
        console.log('setOrgsList called')
            this.orgsFiltered = this.orgs;
      },
      handleFilter() {
        console.log('filter by total hours')
        //filter the Organizations list by Organization address
        this.orgsFiltered = this.orgs.filter((org) => {
            const totalHours = parseFloat(org.total_hours_per_org);
            return totalHours >= this.total_hours;
        });
        this.updateChart();
      },
      clearFilter() {
        // Resets all the variables
        this.total_hours = ''
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
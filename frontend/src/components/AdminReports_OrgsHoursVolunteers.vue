<template>
    <div class="container1"> 
          <div style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
              Organization Volunteers
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
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='org_name'">Organization</th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_org'">Total hours</th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='num_volunteers'">Number of Volunteers</th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="org in sortedItems" :key="org.org_id" style="text-align:left">
                      <td style="text-align:left"> {{ org.org_name }}</td>
                      <td style="text-align:left"> {{ org.total_hours_per_org }}</td>
                      <td style="text-align:left"> {{ org.num_volunteers }}</td>
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
import { getOrgsHoursVolunteersAPI } from '../api/api.js'
export default {
  name: 'OrgsHoursVolunteers',
  components: {
      LoadingModal,
  },
  data() {
      return {
          orgs: [],
          isLoading: false,
          sortBy: 'num_volunteers',
          sortDesc: false,
          searchBy: '',
          total_hours: null,
          number_of_volunteers: null,
          orgsFiltered: [],
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
        if (field === 'num_volunteers' || field === 'total_hours_per_org') {
            order *= -1;
        }

        // Make a copy of the original array to avoid modifying the original data
        const orgs = this.orgsFiltered.slice();

        // Sort the array by the specified field and order
        orgs.sort((a, b) => {
            if (a[field] < b[field]) return -1 * order;
            if (a[field] > b[field]) return 1 * order;
            return 0;
        });

        return orgs;
    },
  },
  methods: {
      async loadData() {
          this.isLoading = true;
          try {
              const response = await getOrgsHoursVolunteersAPI();
              this.orgs = response.data;
              this.setOrgsList();
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
        console.log('filter handled')
        if (this.searchBy === 'Total Hours') {
            console.log('filter by total hours')
            //filter the Organizations list by Organization name
            this.orgsFiltered = this.orgs.filter((org) => {
                const totalHours = parseFloat(org.total_hours_per_org);
                return totalHours >= this.total_hours;
            });
            console.log('orgsFiltered after filter', this.orgsFiltered)

            } 
            //if user searched by Organization address
            else if (this.searchBy === 'Number of Volunteers') {
                console.log('filter by num volunteers')
                //filter the Organizations list by Organization address
                this.orgsFiltered = this.orgs.filter((org) => {
                    const totalVolunteers = parseFloat(org.num_volunteers);
                    return totalVolunteers >= this.number_of_volunteers;
                });
            }
      },
      clearFilter() {
            // Resets all the variables
            this.searchBy = ''
            this.total_hours = ''
            this.number_of_volunteers = ''
            this.setOrgsList()
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
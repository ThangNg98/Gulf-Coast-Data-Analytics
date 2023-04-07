<template>
    <div class="container1"> 
          <div style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
              Organization Hours
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
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='org_name'">Organization</th>
                  <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours_per_org'">Hours</th>
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
    </div>

    <div>
      <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getOrgsHoursAPI } from '../api/api.js'
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
              const response = await getOrgsHoursAPI();
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
        console.log('filter by total hours')
        //filter the Organizations list by Organization address
        this.orgsFiltered = this.orgs.filter((org) => {
            const totalHours = parseFloat(org.total_hours_per_org);
            return totalHours >= this.total_hours;
        });
      },
      clearFilter() {
            // Resets all the variables
            this.total_hours = ''
            this.setOrgsList();
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
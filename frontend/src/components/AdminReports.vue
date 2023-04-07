<template>
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
            Select Report
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
            <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsHours = !showOrgsHours">Organization Hours Report</button></li>
            <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsVolunteers = !showOrgsVolunteers">Organization Volunteers Report</button></li>
            <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsHoursVolunteers = !showOrgsHoursVolunteers">Organization Hours and Volunteers Report</button></li>
        </ul>
    </div>

    <OrgsHours v-if="showOrgsHours"/>
    
    <OrgsVolunteers v-if="showOrgsVolunteers"/>

    <OrgsHoursVolunteers v-if="showOrgsHoursVolunteers" />
</template>

<script>
import OrgsHours from './AdminReports_OrgsHours.vue'
import OrgsVolunteers from './AdminReports_OrgsVolunteers.vue'
import OrgsHoursVolunteers from './AdminReports_OrgsHoursVolunteers.vue'
export default {
    name: 'Reports',
    components: {
        OrgsHours,
        OrgsVolunteers,
        OrgsHoursVolunteers
    },
    data() {
        return {
            showOrgsHours: false,
            showOrgsVolunteers: false,
            showOrgsHoursVolunteers: false,
        }
    },
    mounted() {
        
    },
    methods: {
        clearComponents() {
            this.showOrgsHours = false;
            this.showOrgsVolunteers = false;
            this.showOrgsHoursVolunteers = false;
        }
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
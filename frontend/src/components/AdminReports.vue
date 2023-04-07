<template>
    <button @click="clearComponents(); showOrgsHours = !showOrgsHours">Click me to show OrgsHours</button>
    <div></div>
    <button @click="clearComponents(); showOrgsVolunteers = !showOrgsVolunteers">Click me to show OrgsVolunteers</button>
    <div></div>
    <button @click="clearComponents(); showOrgsHoursVolunteers = !showOrgsHoursVolunteers">Click me to show OrgsHoursVolunteers</button>

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
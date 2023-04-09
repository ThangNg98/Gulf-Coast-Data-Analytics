<template>
    <div class="dropdown-container">
        <div class="dropdown">
            <button class="btn btn-secondary btn-lg dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
                Select Report
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showDatesHours = !showDatesHours">Dates by Total Hours Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsHours = !showOrgsHours">Organizations - Hours Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsVolunteers = !showOrgsVolunteers">Organizations - Volunteers Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showOrgsHoursVolunteers = !showOrgsHoursVolunteers">Organizations - Hours and Volunteers Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showEventsHours = !showEventsHours">Events - Hours Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showEventsVolunteers = !showEventsVolunteers">Events - Volunteers Report</button></li>
                <li><button class="dropdown-item" type="button" @click="clearComponents(); showEventsHoursVolunteers = !showEventsHoursVolunteers">Events - Hours and Volunteers Report</button></li>
            </ul>
        </div>
    </div>

    <div v-if="!showOrgsHours && !showOrgsHoursVolunteers && !showEventsHours && !showEventsVolunteers && !showEventsHoursVolunteers && !showDatesHours"><h6>Please select a report</h6></div>

    <OrgsHours v-if="showOrgsHours"/>
    
    <OrgsVolunteers v-if="showOrgsVolunteers"/>

    <OrgsHoursVolunteers v-if="showOrgsHoursVolunteers" />

    <EventsHours v-if="showEventsHours" />

    <EventsVolunteers v-if="showEventsVolunteers" />

    <EventsHoursVolunteers v-if="showEventsHoursVolunteers" />

    <DatesHours v-if="showDatesHours" />
</template>

<script>
import OrgsHours from './AdminReports_OrgsHours.vue'
import OrgsVolunteers from './AdminReports_OrgsVolunteers.vue'
import OrgsHoursVolunteers from './AdminReports_OrgsHoursVolunteers.vue'
import EventsHours from './AdminReports_EventsHours.vue'
import EventsVolunteers from './AdminReports_EventsVolunteers.vue'
import EventsHoursVolunteers from './AdminReports_EventsHoursVolunteers.vue'
import DatesHours from './AdminReports_DatesHours.vue'
export default {
    name: 'Reports',
    components: {
        OrgsHours,
        OrgsVolunteers,
        OrgsHoursVolunteers,
        EventsHours,
        EventsVolunteers,
        EventsHoursVolunteers,
        DatesHours,
    },
    data() {
        return {
            showOrgsHours: false,
            showOrgsVolunteers: false,
            showOrgsHoursVolunteers: false,
            showEventsHours: false,
            showEventsVolunteers: false,
            showEventsHoursVolunteers: false,
            showDatesHours: false,
        }
    },
    mounted() {
        
    },
    methods: {
        clearComponents() {
            this.showOrgsHours = false;
            this.showOrgsVolunteers = false;
            this.showOrgsHoursVolunteers = false;
            this.showEventsHours = false;
            this.showEventsVolunteers = false;
            this.showEventsHoursVolunteers = false;
            this.showDatesHours = false;
        }
    },
}
</script>

<style>
.dropdown-container {
    display: flex;
    justify-content: center;
    margin-bottom: 2vw;
}



.dropdown-menu {
    border: none;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
    border-radius: 0.25rem;
}

.dropdown-item {
    font-size: 16px;
    font-weight: 500;
    padding-top: 8px;
    padding-bottom: 8px;
}
</style>
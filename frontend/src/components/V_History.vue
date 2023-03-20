<template>
    <div class="container">
        <h3>Total Hours Overall: {{ totalHours }}</h3>
        <div><SessionsTable></SessionsTable></div>
        <br>

        <h3>Total Hours per Organization</h3>
        <div><HoursPerOrg></HoursPerOrg></div>
        <br>

        <h3>Total Hours Per Year</h3>
        <div><HoursPerYear></HoursPerYear></div>
        
    </div>
</template>
<script>
    import HoursPerOrg from './V_HoursPerOrgChart.vue';
    import HoursPerYear from './V_HoursPerYearChart.vue';
    import SessionsTable from './V_SessionsTable.vue';
    export default {
        components: {
            HoursPerOrg,
            HoursPerYear,
            SessionsTable
        },
        data() {
            return {
                totalHours: 15 //use axios to get total hours
            }
        },
    }
</script>
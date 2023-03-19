<template>
    <div class="mb-3"><h5>Total Hours Overall: </h5></div>
    <SessionsTable></SessionsTable>
    <div>
        <div class="mt-5"><HoursPerOrg></HoursPerOrg></div>
        <div class="mt-5"><HoursPerYear></HoursPerYear></div>
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
                
            }
        },
    }
</script>
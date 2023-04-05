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

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

</template>
<script>
    import HoursPerOrg from './V_HoursPerOrgChart.vue';
    import HoursPerYear from './V_HoursPerYearChart.vue';
    import SessionsTable from './V_SessionsTable.vue';
    import UpdateModal from './UpdateModal.vue';
    export default {
        components: {
            HoursPerOrg,
            HoursPerYear,
            SessionsTable,
            UpdateModal
        },
        data() {
            return {
                totalHours: 15, //use axios to get total hours
                updateModal: false,
                title: '',
                message: '',
            }
        },
        mounted() {
            console.log('history mounted')
            const query = new URLSearchParams(this.$route.query);
            if (query.get('update') === 'true') {
                console.log('update is true')
                this.updateModal = true;
                this.title = "Updated!"
                this.message = "You have updated your information."
            }
        },
        methods: {
            closeUpdateModal() {
                this.updateModal = false;
                this.title = '';
                this.message = '';
            },
        }
    }
</script>
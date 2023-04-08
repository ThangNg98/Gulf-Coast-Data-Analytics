<template>
    <div>
        <div class="d-flex justify-content-center">
            <div class="d-inline-flex flex-column w-75 text-start" style="min-width:300px">
                <h6>Hours per Month in the Last Six Months</h6>
                <!--named 'HoursPerYear' but data is sessions per month in the last six months-->
                <div><HoursPerYear :listOfMonths="this.listOfMonths" :listOfHours="this.listOfHours"></HoursPerYear></div>
                <br>
                <!--session history from the last six months-->
                <h6>Session History From the Last Six Months</h6>
                <div><SessionsTable :sessions="this.sessions"></SessionsTable></div>
            </div>
        </div>
    </div>

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

</template>
<script>
    import HoursPerYear from './V_HoursPerYearChart.vue';
    import SessionsTable from './V_SessionsTable.vue';
    import UpdateModal from './UpdateModal.vue';
    import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore'
import axios from 'axios';

    export default {
        components: {
            HoursPerYear,
            SessionsTable,
            UpdateModal
        },
        data() {
            return {
                volunteer_id: useVolunteerPhoneStore().volunteerID,
                totalHours: 15, //use axios to get total hours
                updateModal: false,
                title: '',
                message: '',
                sessions: [], //use axios to get a list of session information
                listOfHours: [], //use axios to get list of hours in the same order as months
                listOfMonths: [], //use axios to get list of months this volunteer has worked in
            }
        },
        created() {
            this.getInfo();
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
            async getInfo() {
                const session_hist_response = await axios.get(`http://127.0.0.1:5000/get_6months_session_history/${this.volunteer_id}`);
                this.sessions = session_hist_response.data;
                const hours_hist_response = await axios.get(`http://127.0.0.1:5000/get_6months_hours_history/${this.volunteer_id}`);
                //console.log(hours_hist_response.data);
                /*for (var i = 0; i < hours_hist_response.data.length; i++) {
                    console.log(JSON.parse(hours_hist_response.data[i].hours));
                    console.log(this.listOfHours)
                    this.listOfHours.push(JSON.parse(hours_hist_response.data[i].hours))
                }*/
                this.putLists(hours_hist_response.data);
            },
            putLists(data) {
                console.log(data);
                for (var i = 0; i < data.length; i++) {
                    console.log(JSON.parse(data[i].hours));
                    this.listOfHours.push(1);
                }
            }
        }
    }
</script>
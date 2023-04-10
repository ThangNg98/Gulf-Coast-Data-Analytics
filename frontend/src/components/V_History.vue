<template>
    <div v-if="isLoaded">
        <div class="d-flex justify-content-center">
            <div class="d-inline-flex flex-column w-75 text-start" style="min-width:300px">
                <!--graph: named 'HoursPerYear' but data is sessions per month in the last six months-->
                <div v-if="isLoaded">
                <h6>Hours per Month in the Last Six Months</h6><HoursPerYear :listOfMonths="this.listOfMonths.reverse()" :listOfHours="this.listOfHours.reverse()"></HoursPerYear></div>
                <br>
                <!--table: session history from the last six months-->
                <div><h6>Session History From the Last Six Months</h6><SessionsTable :sessions="this.sessions"></SessionsTable></div>
            </div>
        </div>
    </div>
    
    <div>
            <LoadingModal v-if="!isLoaded"></LoadingModal>
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
    import LoadingModal from './LoadingModal.vue'
    import axios from 'axios';

    export default {
        components: {
            HoursPerYear,
            SessionsTable,
            UpdateModal,
            LoadingModal,
        },
        data() {
            return {
                volunteer_id: useVolunteerPhoneStore().volunteerID,
                totalHours: 15, //use axios to get total hours
                updateModal: false,
                title: '',
                message: '',
                sessions: [], //use axios to get a list of session information
                hours_data: [],
                listOfHours: [], //use axios to get list of hours in the same order as months
                listOfMonths: [], //use axios to get list of months this volunteer has worked in
                isLoaded: false,
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
                try {
                    this.getSessionHistory();
                } catch(error) {
                    console.log(error)
                }
                const session_hist_response = await axios.get(`http://127.0.0.1:5000/get_6months_session_history/${this.volunteer_id}`);
                this.sessions = session_hist_response.data;
                const hours_hist_response = await axios.get(`http://127.0.0.1:5000/get_6months_hours_history/${this.volunteer_id}`);
                //console.log(hours_hist_response.data);
                for (var i = 0; i < hours_hist_response.data.length; i++) {
                    //hours
                    this.listOfHours.push(JSON.parse(hours_hist_response.data[i].hours));
                    //months
                    this.listOfMonths.push(hours_hist_response.data[i].month);
                }
                this.isLoaded = true;
            }
        }
    }
</script>
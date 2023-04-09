<!--'/admindashview'-->
<template>
    <div class="container">
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <div class="d-flex flex-row">
            <!--monthly history table-->
            <div class="mb-3 w-50 p-4">
                <div>
                <h6 class="text-center">Monthly History in the Last 6 Months</h6>
                <MonthlyTable :monthlyData="this.monthlyData" v-if="isLoaded"></MonthlyTable></div>
            </div>
            <!--graphs-->
            <div class="mb-3 w-50 p-4">
                <!--unique volunteers-->
                <div>
                    <h6 class="text-center">Number of Volunteers per Month in the Last 6 Months</h6>
                    <MonthlyUniqueVolunteersChart :months="this.months" :volunteers="this.volunteers" :totalVolunteers="this.totalVolunteers" v-if="isLoaded"></MonthlyUniqueVolunteersChart>
                </div>
                <!--org donut-->
                <div class="mt-5">
                    <h6 class="text-center">Number of Hours per Organization in the Last 6 Months</h6>
                    <MonthlyOrgsChart :orgNames="this.orgNames" :orgHours="this.orgHours" v-if="isLoaded"></MonthlyOrgsChart>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
import MonthlyOrgsChart from "@/components/AdminChartOfOrgs.vue"
import { useAdminLoginStore } from '@/stores/AdminLoginStore'
import axios from 'axios';

    export default {
        name: 'Admin Dashboard View',
        components: {
            MonthlyTable,
            MonthlyUniqueVolunteersChart,
            MonthlyOrgsChart,
        },
        data() {
            return {
                months: [], // get past 12 months
                volunteers: [], // get past total hours for months
                totalVolunteers: [],
                monthlyData: [ //use axios to get the data
                    {
                        MonthName: '',
                        YearName: null,
                        TotalHours: null
                    }
                ],
                orgNames: ['No Organization'],
                orgHours: [],
                isLoaded: false,
            }
        },
        created() {
            this.getInfo();
            console.log('isLoggedIn store at DashView: ', useAdminLoginStore().isLoggedIn);
        },
        methods: {
            async getInfo() {
                await axios.get('http://127.0.0.1:5000/get_hist_6')
                    .then(response => {
                        this.monthlyData = response.data;
                        for (var i = 0; i < response.data.length; i++) {
                            this.months.push(response.data[i].MonthName);
                            this.volunteers.push(response.data[i].UniqueVolunteers);
                            this.totalVolunteers.push(response.data[i].TotalVolunteers);
                        }
                })
                await axios.get('http://127.0.0.1:5000/get_orgs_6')
                    .then(response => {
                        for (var i = 0; i < response.data.length; i++) {
                            if (response.data[i].orgNames) {
                                this.orgNames.push(response.data[i].orgNames);
                            }
                            this.orgHours.push(response.data[i].orgHours);
                        }
                    })
                this.isLoaded = true;
                }
            }
    }
</script>

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
}
</style>
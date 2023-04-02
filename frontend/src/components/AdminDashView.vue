<!--'/admindashview'-->
<template>
        <div class="container">
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <div>
            <!--monthly history table-->
            <h6 class="text-center">Monthly History</h6>
            <div class="mb-3"><MonthlyTable></MonthlyTable></div>
            <h6 class="text-center">Total Hours per Month in the Last Year</h6>
            <div class="mb-3"><MonthlyHoursChart></MonthlyHoursChart></div>
            <h6 class="text-center">Number of Unique Volunteers per Month in the Last Year</h6>
            <div class="mb-3"><MonthlyUniqueVolunteersChart></MonthlyUniqueVolunteersChart></div>
        </div>
    </div>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
import MonthlyHoursChart from "@/components/AdminChartOfHoursPerMonth.vue"
import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

    export default {
        name: 'Admin Dashboard View',
        components: {
            MonthlyTable,
            MonthlyHoursChart,
            MonthlyUniqueVolunteersChart
        },
        created() {
            console.log('isLoggedIn store at DashView: ', useAdminLoginStore().isLoggedIn)
        }
    }
</script>
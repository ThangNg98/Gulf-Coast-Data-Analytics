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
            <!--last year's total hours-->
            <h6 class="text-center">Total Hours per Month in the Last Year</h6>
            <div class="mb-3"><MonthlyHoursChart></MonthlyHoursChart></div>
            <!--last year's total unique volunteers-->
            <h6 class="text-center">Number of Unique Volunteers per Month in the Last Year</h6>
            <div class="mb-3"><MonthlyUniqueVolunteersChart></MonthlyUniqueVolunteersChart></div>
        </div>
    </div>
</template>
<script>
//import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
//import MonthlyHoursChart from "@/components/AdminChartOfHoursPerMonth.vue"
//import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
import { useAdminLoginStore } from '@/stores/AdminLoginStore'
import { defineAsyncComponent } from "vue"

//const MonthlyTable = await import("@/components/AdminMonthlyHistoryTable.vue");
//const MonthlyHoursChart = await import("@/components/AdminChartOfHoursPerMonth.vue");

    export default {
        name: 'Admin Dashboard View',
        components: {
            MonthlyTable: defineAsyncComponent(() => import('@/components/AdminMonthlyHistoryTable.vue')),
            MonthlyHoursChart: defineAsyncComponent(() => import("@/components/AdminChartOfHoursPerMonth.vue")),
            MonthlyUniqueVolunteersChart: defineAsyncComponent(() => import('@/components/AdminChartOfUniqueVolunteers.vue'))
        },
        created() {
            console.log('isLoggedIn store at DashView: ', useAdminLoginStore().isLoggedIn)
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
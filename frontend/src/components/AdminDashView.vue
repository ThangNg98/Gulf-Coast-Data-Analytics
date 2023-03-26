<!--'/admindashview'-->
<template>
        <div class="container text-center">
        <div>
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <div>
            <!--monthly history table-->
            <div class="mb-3"><MonthlyTable></MonthlyTable></div>
            <div class="mb-3"><MonthlyHoursChart></MonthlyHoursChart></div>
            <div class="mb-3"><MonthlyUniqueVolunteersChart></MonthlyUniqueVolunteersChart></div>
        </div>
    </div>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
import MonthlyHoursChart from "@/components/AdminChartOfHoursPerMonth.vue"
import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
    export default {
        name: 'Admin Dashboard View',
        components: {
            MonthlyTable,
            MonthlyHoursChart,
            MonthlyUniqueVolunteersChart
        }
    }
</script>
<!--'/admindash'-->
<template>
    <main class="text-center">
        <div>
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <!--monthly history table-->
        <MonthlyTable></MonthlyTable>
        <MonthlyHoursChart></MonthlyHoursChart>
        <MonthlyUniqueVolunteersChart></MonthlyUniqueVolunteersChart>
    </main>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
import MonthlyHoursChart from "@/components/AdminChartOfHoursPerMonth.vue"
import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
    export default {
        components: {
            MonthlyTable,
            MonthlyHoursChart,
            MonthlyUniqueVolunteersChart
        }
    }
</script>
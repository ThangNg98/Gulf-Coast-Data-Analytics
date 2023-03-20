<!--'/admindash'-->
<template>
    <main class="text-center">
        <div>
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <!--monthly history table-->
        <MonthlyTable></MonthlyTable>
    </main>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
    export default {
        components: {
            MonthlyTable
        }
    }
</script>
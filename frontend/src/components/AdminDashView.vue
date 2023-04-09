<!--'/admindashview'-->
<template>
    <div class="container">
        <div class="text-center">
            <h1 style="margin-top: 2rem; margin-bottom: 2rem">Admin Dashboard</h1>
        </div>
        <div class="d-flex flex-row">
            <!--monthly history table-->
            <div class="mb-3 w-50 p-5">
                <h6 class="text-center">Monthly History in the Last 6 Months</h6>
                <MonthlyTable ref="componentA"></MonthlyTable>
            </div>
            <!--graphs-->
            <div class="mb-3 w-50 p-5">
                <!--unique volunteers-->
                <div class="w-100 h-auto">
                    <h6 class="text-center">Number of Volunteers per Month in the Last 6 Months</h6>
                    <MonthlyUniqueVolunteersChart ref="componentB" v-if="componentBVisible"></MonthlyUniqueVolunteersChart>
                </div>
                <!--org donut-->
                <div class="mt-3">
                    donut here
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import MonthlyTable from "@/components/AdminMonthlyHistoryTable.vue"
import MonthlyUniqueVolunteersChart from "@/components/AdminChartOfUniqueVolunteers.vue"
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

    export default {
        name: 'Admin Dashboard View',
        components: {
            MonthlyTable,
            MonthlyUniqueVolunteersChart
        },
        data() {
            return {
                componentBVisible: false
            }
        },
        created() {
            console.log('isLoggedIn store at DashView: ', useAdminLoginStore().isLoggedIn);
        },
        async mounted() {
            console.log('mounted')
            await this.$refs.componentA.load().then(async () => {
                this.componentBVisible = true;
                await this.$refs.componentB;
            });
        },
    }
</script>

<style scoped>
.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
}
</style>
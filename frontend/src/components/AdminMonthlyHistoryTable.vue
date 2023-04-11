<template>
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered text-start" style="margin:auto;">
                    <thead class="theadsticky" style="background-color: #e6e7eb !important;">
                    <tr>
                    <th scope="col">Month, Year</th>
                    <th style="text-align:right" scope="col">Total Hours</th>
                    </tr>
                </thead>
                <tbody>
                    <!--use axios data to print rows of monthly data-->
                    <tr v-for="month in monthlyData">
                        <td >{{month.MonthName}}, {{month.YearName}}</td>
                        <td style="width:30%" class="text-end">{{month.TotalHours}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
</template>
<script lang="ts">
    export default {
        props: {
            monthlyData: {
                type: Object,
                keys: {
                    MonthName: String,
                    YearName: Number,
                    TotalHours: Number,
                }
            }
        }
    }
</script>
<template>
    <div class="table-responsive">
            <table class="table w-100">
                <thead>
                    <tr>
                    <th scope="col">Month, Year</th>
                    <th scope="col">Total Hours Worked</th>
                    <th scope="col">Number of Unique Volunteers</th>
                    </tr>
                </thead>
                <tbody>
                    <!--use axios data to print rows of monthly data-->
                    <tr v-for="month in monthlyData">
                        <td>{{month.MonthName}}, {{month.YearName}}</td>
                        <td>{{month.TotalHours}}</td>
                        <td>{{month.UniqueVolunteers}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
</template>
<script lang="ts">
import axios from 'axios';
    export default {
        data() {
            return {
                monthlyData: [ //use axios to get the data
                    {
                        MonthName: '',
                        YearName: null,
                        TotalHours: null,
                        UniqueVolunteers: null
                    }
                ]
            }
        },
        methods: {
            getMonthsHoursUniques() {
                axios.get('http://127.0.0.1:5000/get_month_hours_uniques')
                .then(response => {
                    this.monthlyData = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },
        mounted() {
            this.getMonthsHoursUniques();
        }
    }
</script>
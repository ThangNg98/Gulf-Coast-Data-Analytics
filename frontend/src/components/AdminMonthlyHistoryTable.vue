<template>
    <div class="table-responsive">
            <table class="table w-100">
                <caption class="ms-5">Monthly History</caption>
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
                        <td>{{month.month}}, {{month.year}}</td>
                        <td>{{month.totalHours}}</td>
                        <td>{{month.totalUniqueVolunteers}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
</template>
<script lang="ts">
    export default {
        data() {
            return {
                monthlyData: [ //use axios to get the data
                    {
                        month: 'January',
                        year: 2023,
                        totalHours: 200,
                        totalUniqueVolunteers: 55
                    },
                    {
                        month: 'February',
                        year: 2023,
                        totalHours: 100,
                        totalUniqueVolunteers: 30
                    },
                    {
                        month: 'March',
                        year: 2023,
                        totalHours: 150,
                        totalUniqueVolunteers: 35
                    },
                    {
                        month: 'April',
                        year: 2023,
                        totalHours: 100,
                        totalUniqueVolunteers: 10
                    },
                    {
                        month: 'May',
                        year: 2023,
                        totalHours: 250,
                        totalUniqueVolunteers: 45
                    }
                ]
            }
        }
    }
</script>
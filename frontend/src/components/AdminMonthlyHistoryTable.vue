<template>
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered text-start" style="margin:auto;">
                    <thead class="theadsticky" style="background-color: #e6e7eb !important;">
                    <tr>
                    <th scope="col">Month, Year</th>
                    <th scope="col">Total Hours Worked</th>
                    </tr>
                </thead>
                <tbody>
                    <!--use axios data to print rows of monthly data-->
                    <tr v-for="month in monthlyData">
                        <td>{{month.MonthName}}, {{month.YearName}}</td>
                        <td class="text-end">{{month.TotalHours}}</td>
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
                        TotalHours: null
                    }
                ]
            }
        },
        methods: {
            async load() {
                await axios.get('http://127.0.0.1:5000/get_hist_6')
                .then(response => {
                    this.monthlyData = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },
        created() {
        }
    }
</script>
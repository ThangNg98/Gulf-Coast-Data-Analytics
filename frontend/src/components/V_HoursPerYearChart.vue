<template>
    <h5>Hours Per Year</h5>
    <canvas id="hoursPerYear"></canvas>
</template>
<script>
import Chart from 'chart.js/auto';
export default {
    mounted() {
        const ctx = document.getElementById('hoursPerYear');

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: this.listOfYears,
            datasets: [{
            label: '# of Hours',
            data: this.listOfHours,
            borderWidth: 1
            }]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
        });
    },
    data() {
        return {
            listOfYears: ['2020', '2022', '2023'], //use axios to get list of years this volunteer has worked in
            listOfHours: [120, 50, 100], //use axios to get list of hours in the same order as years
        }
    }
}
</script>
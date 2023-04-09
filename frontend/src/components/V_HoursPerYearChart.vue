<template>
    <canvas id="hoursPerYear"></canvas>
</template>
<script>
import Chart from 'chart.js/auto';
export default {
    mounted() {
        const ctx = document.getElementById('hoursPerYear');
        new Chart(ctx, {
        type: 'line',
        data: {
            labels: this.listOfMonths,
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
    props: {
        listOfMonths: Object,
        listOfHours: Object,
    },
    data() {
        return {
        }
    }
}
</script>
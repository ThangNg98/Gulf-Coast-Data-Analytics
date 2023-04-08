<template>
    <canvas id="hoursPerYear"></canvas>
</template>
<script>
import Chart from 'chart.js/auto';
import { isProxy, toRaw } from 'vue';
export default {
    mounted() {
        const ctx = document.getElementById('hoursPerYear');

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: toRaw(this.listOfMonths),
            datasets: [{
            label: '# of Hours',
            data: toRaw(this.listOfHours),
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
        listOfMonths: Array,
        listOfHours: Array,
    },
    data() {
        return {
        }
    }
}
</script>
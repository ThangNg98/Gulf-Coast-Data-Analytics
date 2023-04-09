<template>
    <div>
        <canvas id="monthlyOrgs"></canvas>
    </div>
</template>
<script>
import Chart from 'chart.js/auto';
import ChartDataLabels from 'chartjs-plugin-datalabels';
    export default {
        props: {
            orgNames: Array,
            orgHours: Array,
        },
        mounted() {
            const ctx = document.getElementById('monthlyOrgs');
            new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: this.orgNames,
                datasets: [{
                    label: 'Total Hours',
                    data: this.orgHours,
                    backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)'
                    ],
                }],
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                    }
                },
                
            }
            });
        }
    }
</script>
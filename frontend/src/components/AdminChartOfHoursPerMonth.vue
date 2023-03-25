<template>
    <div>
        <canvas id="monthlyHours"></canvas>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto';
    export default {
        data() {
            return {
                months: ['January', 'February', 'March', 'April', 'May'], // get past ~5 months
                hours: ['200', '100', '150', '100', '250'], // get past total hours for months
            }
        },
        mounted() {
            const ctx = document.getElementById('monthlyHours');

            new Chart(ctx, {
                type: 'bar',
                data: {
                labels: this.months,
                datasets: [{
                    label: '# of Hours',
                    data: this.hours,
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
        }
    }
</script>
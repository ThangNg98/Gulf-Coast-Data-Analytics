<template>
    <div>
        <canvas id="monthlyVolunteers"></canvas>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto';
    export default {
        data() {
            return {
                months: ['January', 'February', 'March', 'April', 'May'], // get past ~5 months
                volunteers: ['55', '30', '35', '10', '45'], // get past total hours for months
            }
        },
        mounted() {
            const ctx = document.getElementById('monthlyVolunteers');

            new Chart(ctx, {
                type: 'bar',
                data: {
                labels: this.months,
                datasets: [{
                    label: '# of Unique Volunteers',
                    data: this.volunteers,
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
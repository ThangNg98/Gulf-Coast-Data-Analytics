<template>
    <div>
        <canvas id="monthlyHours"></canvas>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto';
    import axios from 'axios';
    export default {
        data() {
            return {
                months: ['January', 'February', 'March', 'April'], // get past 12 months
                hours: ['100', '200', '150', '175'], // get past total hours for months
            }
        },
        methods: {
            getMonthsHoursUniques() {
                axios.get('http://127.0.0.1:5000/get_past_year')
                .then(response => {
                    const res = response.data;
                    console.log(res);
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },
        mounted() {
            this.getMonthsHoursUniques();
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
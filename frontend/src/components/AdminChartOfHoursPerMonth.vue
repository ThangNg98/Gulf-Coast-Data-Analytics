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
                months: [], // get past 12 months
                hours: [], // get past total hours for months
            }
        },
        methods: {
            async load() {
                await axios.get('http://127.0.0.1:5000/get_past_year')
                .then(response => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.months.push(response.data[i].MonthName);
                        this.hours.push(response.data[i].TotalHours);
                    }
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
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },
        created() {
            this.load();
        }
    }
</script>
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
                months: [], // get past 12 months
                volunteers: [], // get past total hours for months
            }
        },
        methods: {
            async getPastYear() {
                await axios.get('http://127.0.0.1:5000/get_past_year')
                .then(response => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.months.push(response.data[i].MonthName);
                        this.volunteers.push(response.data[i].UniqueVolunteers);
                    }
                    const ctx = document.getElementById('monthlyVolunteers');

                    new Chart(ctx, {
                        type: 'bar',
                        data: {
                        labels: this.months,
                        datasets: [{
                            label: '# of Unique Volunteers',
                            data: this.volunteerss,
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
        mounted() {
            this.getPastYear();
        }
    }
</script>
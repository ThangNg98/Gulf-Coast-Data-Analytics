<template>
    <div>
        <canvas id="monthlyVolunteers"></canvas>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto';
    import axios from 'axios';
    export default {
        data() {
            return {
                months: [], // get past 12 months
                volunteers: [], // get past total hours for months
                totalVolunteers: [],
            }
        },
        methods: {
            async load() {
                await axios.get('http://127.0.0.1:5000/get_hist_6')
                .then(response => {
                    for (var i = 0; i < response.data.length; i++) {
                        this.months.push(response.data[i].MonthName);
                        this.volunteers.push(response.data[i].UniqueVolunteers);
                        this.totalVolunteers.push(response.data[i].TotalVolunteers);
                    }
                    const ctx = document.getElementById('monthlyVolunteers');

                    new Chart(ctx, {
                        type: 'line',
                        data: {
                        labels: this.months,
                        datasets: [
                            {
                                label: '# of Unique Volunteers',
                                data: this.volunteers,
                                borderWidth: 1
                            },
                            {
                                label: '# of Total Volunteers',
                                data: this.totalVolunteers,
                                borderWidth: 1
                            }
                    ]
                        },
                        options: {
                        responsive: true,
                        interaction: {
                            mode: 'index',
                            intersect: false,
                        },
                        stacked: false,
                        scales: {
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                        },
                        }
                    }});
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
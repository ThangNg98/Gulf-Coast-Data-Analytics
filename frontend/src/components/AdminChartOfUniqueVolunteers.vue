<template>
    <div>
        <canvas id="monthlyVolunteers"></canvas>
    </div>
</template>
<script>
    import Chart from 'chart.js/auto';
    export default {
        props: {
            months: Array,
            volunteers: Array,
            totalVolunteers: Array,
        },
        mounted() {
            const ctx = document.getElementById('monthlyVolunteers');

            new Chart(ctx, {
                type: 'line',
                data: {
                labels: this.months.reverse(),
                datasets: [
                    {
                        label: '# of Unique Volunteers',
                        data: this.volunteers.reverse(),
                        borderWidth: 1
                    },
                    {
                        label: '# of Total Volunteers',
                        data: this.totalVolunteers.reverse(),
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
        }
    }
</script>
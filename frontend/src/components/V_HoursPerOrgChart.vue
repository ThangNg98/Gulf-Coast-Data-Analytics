<template>
    <canvas id="hoursPerOrg"></canvas>
</template>
<script>
import Chart from 'chart.js/auto';
export default {
    mounted() {
        const ctx = document.getElementById('hoursPerOrg');

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: this.listOfOrgs,
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
    data() {
        return {
            listOfOrgs: ['Org1', 'Org2', 'Org3', 'Other', 'No Org'], //use axios to get list of orgs this volunteer has worked for
            listOfHours: [12, 19, 3, 5, 2, 3], //use axios to get list of hours in the same order as orgs
        }
    }
}
</script>
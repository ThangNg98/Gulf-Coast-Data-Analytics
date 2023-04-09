<template>

<div class="main-container">
  <div class="form-container">
    <div class="row mb-3">
        <h2>
            Total Hours by Date
            <small class="text-muted">Report</small>
        </h2>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-md-6">
        <div class="text-start">
            <label for="start-date" class="form-label">Start Date:</label>
        </div>
        <input type="date" ref="start-date" v-model="startDate" :disabled="currentlySearched" class="form-control" :class="{ 'is-invalid': errors.Start }">
        <div class="invalid-feedback">{{errors.Start}}</div>
      </div>
      <div class="col-12 col-md-6">
        <div class="text-start">
            <label for="end-date" class="form-label">End Date:</label>
        </div>
        <input type="date" ref="end-date" v-model="endDate" :disabled="currentlySearched" class="form-control" :class="{ 'is-invalid': errors.End }">
        <div class="invalid-feedback">{{errors.End}}</div>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-md-6">
        <div class="text-start">
            <label for="grouping" class="form-label">Group by:</label>
        </div>
        <select id="grouping" v-model="tempGrouping" :disabled="currentlySearched" class="form-select">
          <option value="day">Daily</option>
          <option value="week">Weekly</option>
          <option value="month">Monthly</option>
          <option value="quarter">Quarterly</option>
          <option value="year">Yearly</option>
        </select>
      </div>
      <div class="col-12 col-md-6 d-flex align-items-center">
        <div class="d-md-flex">
            <div class="text-start">
                <label for="fill-missing-dates" class="form-check-label ms-2">Include Time Periods with 0 Hours:</label>
            </div>
            <div class="form-check ms-md-3">
                <input type="checkbox" id="fill-missing-dates" v-model="fillMissingDates" :disabled="currentlySearched" class="form-check-input">
            </div>
        </div>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12">
        <div class="button-container mt-2 d-flex justify-content-end gap-3">
          <button @click="clearFilter" class="btn btn-outline-secondary">
            Clear Search
          </button>
          <button @click="handleFilter" :disabled="currentlySearched" class="btn btn-primary">
            Apply Search
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="container1" v-if="showTable">
        <div class="table-container">
            <div class="table-responsive-md">
                <table class="table table-striped table-hover" style="margin:auto; text-align: center; max-width: 50%;">
                    <thead class="theadsticky">
                        <tr>
                            <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" 
                            @click="() => {
                                sortBy = 'date';
                                sortOrder.date *= -1;
                            }"
                            >
                            {{ dateLabel }}
                            <i class="bi bi-calendar3"></i>
                        </th>
                            <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours'">
                                Total Hours
                                <i class="bi bi-sort-numeric-down-alt"></i>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="date in sortedItems" :key="date.session_date" style="text-align:left">
                            <td style="text-align:left"> {{ formatDate(date.session_date) }}</td>
                            <td style="text-align:left"> {{ date.total_hours }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>


    <div class="chart-container" v-show="showTable">
        <canvas ref="chartCanvas"></canvas>
    </div>


    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getDatesHoursAPI } from '../api/api.js'
import { filterAndGroupData } from '../helpers/tableHelpers';
import Chart from 'chart.js/auto';
import { shallowRef } from 'vue';
export default {
    name: 'DatesHours',
    components: {
        LoadingModal,
    },
    data() {
        return {
            dates: [],
            isLoading: false,
            showTable: false,
            dateLabel: '',
            sortBy: 'date',
            sortOrder: {
                date: 1,
                total_hours: -1,
            },
            datesFiltered: [],
            startDate: null,
            endDate: null,
            grouping: 'day',
            tempGrouping: 'day',
            submitPressed: false,
            errors: {},
            fillMissingDates: false,
            currentlySearched: false,
            chart: null,
            chartFirstCreated: false,
        }
    },
    computed: {
        sortedItems() {
            const field = this.sortBy;
            const order = this.sortOrder[field];

            // Make a copy of the original array to avoid modifying the original data
            const dates = this.datesFiltered.slice();

            // Sort the array by the specified field and order
            dates.sort((a, b) => {
                if (field === 'date') {
                    const dateA = new Date(a[field]);
                    const dateB = new Date(b[field]);
                    if (dateA < dateB) return -1 * order;
                    if (dateA > dateB) return 1 * order;
                    return 0;
                } else {
                    if (a[field] < b[field]) return -1 * order;
                    if (a[field] > b[field]) return 1 * order;
                    return 0;
                }
            });

            return dates;
        },
        chartData() {
            // Sort datesFiltered in ascending order by date
            const sortedDatesFiltered = this.datesFiltered.slice().sort((a, b) => {
                const dateA = a.session_date;
                const dateB = b.session_date;

                if (dateA.includes('-Q') && dateB.includes('-Q')) {
                    const [yearA, quarterA] = dateA.split('-');
                    const [yearB, quarterB] = dateB.split('-');
                    const valueA = parseInt(yearA) * 10 + parseInt(quarterA[1]);
                    const valueB = parseInt(yearB) * 10 + parseInt(quarterB[1]);
                    return valueA - valueB;
                }

                return new Date(dateA) - new Date(dateB);
            });

            return {
                labels: sortedDatesFiltered.map((date) => this.formatDate(date.session_date)),
                datasets: [
                    {
                        label: 'Total Hours per Date',
                        data: sortedDatesFiltered.map((date) => parseFloat(date.total_hours)),
                        backgroundColor: 'rgb(54, 162, 235)',
                        borderColor: 'rgb(54, 162, 235, 0.5)',
                        borderWidth: 1,
                    },
                ],
            };
        },

    },
    watch: {
        startDate(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('Start')
                } else {
                    this.addValidationStyle('Start', 'Please enter a start date.')
                }
            }
        },
        endDate(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('End')
                } else {
                    this.addValidationStyle('End', 'Please enter an end date.')
                }
            }
        },
    },
    mounted() {
        this.loadData();
    },
    methods: {
        removeValidationStyle(name) {
            console.log('remove valid')
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        async loadData() {
            this.isLoading = true;
            try {
                const response = await getDatesHoursAPI();
                this.dates = response.data.map(item => ({
                    ...item,
                    total_hours: parseFloat(item.total_hours),
                }));
                this.setDatesList();
                console.log('setDates')
            } catch (error) {
                console.log(error)
            }
            this.isLoading = false;
        },
        setDatesList() {
            if (!this.startDate || !this.endDate || !this.grouping) {
                this.datesFiltered = this.dates;
                return;
            }            

            this.datesFiltered = filterAndGroupData(this.dates, this.startDate, this.endDate, this.grouping, this.fillMissingDates);
            console.log('this.datesFiltered', this.datesFiltered)
        },
        handleFilter() {
            this.errors = {};
            this.submitPressed = true;
            if (!this.startDate && !this.endDate) {
                this.errors.Start = 'Please enter a start date.' 
                this.errors.End = 'Please enter an end date.' 
            } else if (!this.startDate) {
                this.errors.Start = 'Please enter a start date.'
            } else if (!this.endDate) {
                this.errors.End = 'Please enter an end date.'
            } else {
                this.grouping = this.tempGrouping;
                this.currentlySearched = true;
                this.setDatesList();
                if (this.chartFirstCreated === false) {
                    this.chartFirstCreated = true
                    this.createChart();
                } else if (this.chartFirstCreated === true) {
                    this.updateChart();
                }
                this.showTable = true;
            }
        },
        clearFilter() {
            console.log('errors', this.errors)
            console.log('errors', this.errors)
            this.submitPressed = false;
            this.errors = {};
            this.startDate = null;
            this.endDate = null;
            this.grouping = 'day';
            this.currentlySearched = false;
            this.datesFiltered = this.dates;
            this.showTable = false;
        },
        formatDate(dateString) {

            if (this.grouping === 'day') {
                this.dateLabel = 'Day'
            } else if (this.grouping === 'week') {
                this.dateLabel = 'Week'
            } else if (this.grouping === 'month') {
                this.dateLabel = 'Month'
            } else if (this.grouping === 'quarter') {
                this.dateLabel = 'Quarter'
            } else if (this.grouping === 'year') {
                this.dateLabel = 'Year'
            }

            let date;

            if (dateString.includes('-Q')) {
                const [year, quarter] = dateString.split('-');
                date = new Date(year, (parseInt(quarter[1]) - 1) * 3);
                return `${quarter}-${year}`; // Return the formatted quarter string
            } else if (dateString.includes('-')) {
                date = new Date(dateString);
            } else {
                return dateString;
            }

            const monthNames = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ];

            const month = date.getMonth();
            const day = date.getDate();
            const year = date.getFullYear();

            if (this.grouping === 'month') {
                return `${monthNames[month]} - ${year}`;
            }

            if (this.grouping === 'week') {
                const endDate = new Date(date);
                endDate.setDate(endDate.getDate() + 6);
                const endMonth = endDate.getMonth();
                const endDay = endDate.getDate();
                const endYear = endDate.getFullYear();
                return `${monthNames[month]} ${day.toString().padStart(2, '0')}, ${year} - ${monthNames[endMonth]} ${endDay.toString().padStart(2, '0')}, ${endYear}`;
            }

            return `${monthNames[month]} ${day.toString().padStart(2, '0')}, ${year}`;
        },
        createChart() {
        console.log('create chart called')
        console.log('this.$refs.chartCanvas', this.$refs.chartCanvas)
        const ctx = this.$refs.chartCanvas.getContext('2d');
        this.chart = shallowRef(
          new Chart(ctx, {
          type: 'line',
          data: this.chartData,
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
            plugins: {
              legend: {
                display: false, // set the display property to false
              },
            },
          },
        }));
      },
      updateChart() {
        this.chart.data.labels = this.chartData.labels;
        console.log('labels updated')
        this.chart.data.datasets = this.chartData.datasets;
        console.log('data updated')
        this.chart.update();
        console.log('chart updated')
      },
    }
}
</script>

<style>
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.form-container {
  justify-content: center;
  gap: 1rem;
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.error-text {
  color: #dc3545;
}

.container1 {
  justify-content: center;
  margin: auto;
  padding-left: auto;
  padding-right: auto;
}

.table-container {
  height: 50vh;
  overflow: auto;
}

.theadsticky {
  position: sticky;
  top: 0;
  background-color: white !important;
}

.chart-container {
  position: relative;
  max-width: 70%;
  margin: 2rem auto;
  height: 40vh;
}

.error-text {
  color: #dc3545;
  margin-right: 1rem;
}
</style>
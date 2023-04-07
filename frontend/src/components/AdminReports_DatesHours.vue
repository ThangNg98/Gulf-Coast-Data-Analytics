<template>

    <div>
        <!-- <canvas ref="chart"></canvas> -->
        <div>
        <label for="start-date">Start Date:</label>
        <input type="date" id="start-date" v-model="startDate" :disabled="currentlySearched">
        <label for="end-date">End Date:</label>
        <input type="date" id="end-date" v-model="endDate" :disabled="currentlySearched">
        <label for="grouping">Group by:</label>
        <select id="grouping" v-model="tempGrouping" :disabled="currentlySearched">
            <option value="day">Daily</option>
            <option value="week">Weekly</option>
            <option value="month">Monthly</option>
            <option value="quarter">Quarterly</option>
            <option value="year">Yearly</option>
        </select>
        <!-- <button @click="renderChart">Render Chart</button> -->
        </div>
        <label for="fill-missing-dates">Include Time Periods with 0 Hours:</label>
        <input type="checkbox" id="fill-missing-dates" v-model="fillMissingDates" :disabled="currentlySearched">
    </div>

    <div class="mt-5 grid-cols-2">
        <div v-if="errors" style="color: #dc3545;">
            {{ errors }}
        </div>
            <!--Clear Search button-->
            <button
              @click="clearFilter"
            >
              Clear Search
            </button>
            <!--Search Organization button-->
            <button
              @click="handleFilter"
              :disabled="currentlySearched">
              Apply Search
            </button>
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
                            >{{ dateLabel }}</th>
                            <th scope="col" style="text-align:left" :style="{ cursor: 'pointer' }" @click="sortBy ='total_hours'">Total Hours</th>
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


    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>
</template>

<script>
import LoadingModal from './LoadingModal.vue'
import { getDatesHoursAPI } from '../api/api.js'
import { filterAndGroupData } from '../helpers/tableHelpers';
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
            startDate: '',
            endDate: '',
            grouping: 'day',
            tempGrouping: 'day',
            errors: null,
            fillMissingDates: false,
            currentlySearched: false,
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
    },

    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
            this.isLoading = true;
            try {
                const response = await getDatesHoursAPI();
                this.dates = response.data.map(item => ({
                    ...item,
                    total_hours: parseFloat(item.total_hours),
                }));
                this.setDatesList();
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
            if (!this.startDate && !this.endDate) {
                this.errors = 'Please enter a Start and End Date' 
            } else if (!this.startDate) {
                this.errors = 'Please enter a Start Date'
            } else if (!this.endDate) {
                this.errors = 'Please enter an End Date'
            } else {
                this.errors = null;
                this.grouping = this.tempGrouping;
                this.currentlySearched = true;
                this.setDatesList();
                this.showTable = true;
            }
        },
        clearFilter() {
            this.errors = null;
            this.startDate = '';
            this.endDate = '';
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
        }




    }
}
</script>

<style>
.container1 {
margin: auto;
padding-left: auto;
padding-right: auto
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

</style>
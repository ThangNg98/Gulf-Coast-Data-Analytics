<template>
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Event</th>
                    <th scope="col">Organization</th>
                    <th scope="col">Total Hours</th>
                    <th scope="col">Date</th>
                </tr>
            </thead>
            <tbody>
                <!-- for each session, print event name, org name, hours, and formatted date-->
                <tr v-for="session in this.sessions">
                    <td>{{session.eventName}}</td>
                    <td>{{session.orgName}}</td>
                    <td>{{session.hours}}</td>
                    <td>{{ formatDate(session.date) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                sessions: [ //use axios to get a list of session information
                {
                    eventName: 'Sample Event',
                    orgName: 'Sample Organization',
                    hours: 5,
                    date: new Date(),
                },
                {
                    eventName: 'Sample Event 2',
                    orgName: 'Sample Organization 2',
                    hours: 10,
                    date: new Date(2023, 1, 5),
                }
            ]
            }
        },
        methods: {
            formatDate(current) { //assuming Date method, returns formatted date string
                const newDate = `${current.getMonth()+1}/${current.getDate()}/${current.getFullYear()}`;
                return newDate;
            },
            test() {
                const text = 'test';
                return text;
            }
        }
    }
</script>
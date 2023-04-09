<template>
    <div class="table-responsive">
        <table class="table table-hover">
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
                    <td>{{formatDate(session.dateval) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
    export default {
        props: {
            sessions: Object
        },
        methods: {
            formatDate(current) { //assuming Date method, returns formatted date string m/d/yyyy
                var myDate = new Date(current);
                var output = (myDate.getMonth()+1) + "/" + myDate.getDate() + "/" +  myDate.getFullYear();
                return output;
                //return output
            },
            test() {
                const text = 'test';
                return text;
            }
        }
    }
</script>
<template>
    <div class="container1 table-wrapper"> 
    <div class="table-responsive-md">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Date</th>
                    <th scope="col">Event</th>
                    <th scope="col">Organization</th>
                    <th scope="col">Total Hours</th>
                </tr>
            </thead>
            <tbody>
                <!-- for each session, print event name, org name, hours, and formatted date-->
                <tr v-for="session in this.sessions">
                    <td>{{formatDate(session.dateval) }}</td>
                    <td>{{session.eventName}}</td>
                    <td>{{session.orgName}}</td>
                    <td>{{session.hours}}</td>
                </tr>
            </tbody>
        </table>
    </div>
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
                
                var output = (myDate.getMonth()+1) + "/" + (myDate.getDate()+1) + "/" +  myDate.getFullYear();
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

<style scoped>
.table-wrapper {
  max-height: 500px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}

.container1 {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}

</style>
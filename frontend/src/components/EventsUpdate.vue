<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="this.events.event_name">
                <label for="exampleFormControlInput1" class="form-label"> Description</label>
                <textarea class="form-control" id="exampleFormControlInput1" v-model="this.events.event_description"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/events"> Back to Events</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" @click="updateButtonClicked = true">Update</button>
                <button type="submit" class="btn btn-danger" @click="deleteButtonClicked = true">Delete</button>
            </div>
        </form>
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Total Hours</th>
                        <th scope="col">Number of Volunteers</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td v-if="hours != null"> {{ this.hours }}</td>
                            <td v-else> 0 </td>
                            <td v-if="num_volunteers != 0"> {{ this.num_volunteers }}</td>
                            <td v-else> 0 </td>
                        </tr>
                    </tbody>
                </table>
        </div>
        
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'EventsUpdate',
    data() {
        return {
            msg : "Update Event",
            events: {
                event_id: '',
                event_name: '',
                event_description: ''
            },
            updateButtonClicked: false,
            deleteButtonClicked: false,
            hours: null,
            num_volunteers: 0
        };

    },
    created() {
    axios.get(`http://127.0.0.1:5000/get_event/${this.$route.params.event_id}`).then(response => {
        this.events.event_id = response.data[0].event_id;
        this.events.event_name = response.data[0].event_name;
        this.events.event_description = response.data[0].event_description;
        this.hours = response.data[0].total_hours;
        this.num_volunteers = response.data[0].num_volunteers;
    });
    },
    methods: {
        submitForm() {
            if (this.updateButtonClicked == true) {
                this.updateButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/update_event', this.events)
                .then(() =>{
                    this.events={}
                    alert('Event Updated')
                    this.$router.push('/admin/events')
                })
                .catch((error)=>{
                    console.log(error);
                });
            }
            else if (this.deleteButtonClicked == true) {
                this.deleteButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/delete_event', this.events)
                .then(() =>{
                    this.events={}
                    alert('Event Deleted')
                    this.$router.push('/admin/events')
                })
                .catch((error)=>{
                    console.log(error);
                });
            }

        }


    }
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto

}
</style>
<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="events.event_name">

    
                <label for="exampleFormControlInput1" class="form-label"> Description</label>
                <textarea class="form-control" id="exampleFormControlInput1" v-model="events.event_description"></textarea>
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
                            <td>[hours]</td>
                            <td>[# volunteers]</td>
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
                event_id: 2,
                event_name: 'Oasis',
                event_description: 'Blah blah blah'
            },
            updateButtonClicked: false,
            deleteButtonClicked: false
        };

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
                    this.$router.push('/events')
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
                    this.$router.push('/events')
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
<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Garden" v-model="event_info.event_name">

                <label for="exampleFormControlInput1" class="form-label"> Description</label>
                <textarea class="form-control" id="exampleFormControlInput1" placeholder="Living Legacy's Garden" v-model="event_info.event_description"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/events"> Back to Events</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" >Submit</button>
          </div>
        </form>
    </div>
    </main>
</template>

<script>
import axios from "axios";
export default {
    name: 'EventsCreate',
    data() {
        return {
            msg : "Create New Event",
            event_info : {
                event_name: '',
                event_description: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
            .post('https://llc.onrender.com/create_event', this.event_info)
            .then(() =>{
                this.event_info={}
                alert('Event Created')
                this.$router.push('/admin/events')
            })
            .catch((error)=>{
                console.log(error);
            });
        }
    }
}
</script>

<style scoped>
@media only screen and (min-width: 768px) {
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
  width: 25%
}
}
</style>
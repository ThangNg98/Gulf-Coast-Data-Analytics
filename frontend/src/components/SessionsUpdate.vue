<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Session Date</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="3/5/2023">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Start Time</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="2:00 PM">
                    </div>
                    
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Garden">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Finish Time</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="null">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Organization</label>
                        <input type="text" class="form-control" style="max-width: 49%" id="exampleFormControlInput1" placeholder="UH Garden Team">
                    </div>
                </div>
            </div>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/sessions_list"> Back to Sessions</router-link></button>
                <button type="submit" class="btn btn-danger" style="margin-right:0.5rem">Delete</button>
                <button type="submit" class="btn btn-primary" >Update </button>
            </div>
        </form>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'SessionsUpdate',
    data() {
        return {
            msg : "[Volunteer Name]'s Active Session",
            volunteers: {
                first_name: '',
                last_name: '',
                phone:  '',
                email: '',
                emergency_contact_fname: '',
                emergency_contact_lname: '',
                emergency_contact_phone: '',


            },
        };

    },
    methods: {
        submitForm() {

        }


    }
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto;
  text-align: left

}
</style>
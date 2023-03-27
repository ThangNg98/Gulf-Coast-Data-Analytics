<template>
    <div class="container"> 
        <h3>Volunteer</h3>
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.first_name" v-model="new_volunteer_info.first_name">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.last_name" v-model="new_volunteer_info.last_name">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.phone" v-model="new_volunteer_info.phone">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Email</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.email" v-model="new_volunteer_info.email">
                    </div>
                </div>
            </div>
            <br>
            <h3> Emergency Contact</h3>
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.emergency_contact_fname" v-model="new_volunteer_info.emergency_contact_fname">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.emergency_contact_lname" v-model="new_volunteer_info.emergency_contact_lname">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" :placeholder="current_volunteer_info.emergency_contact_phone" v-model="new_volunteer_info.emergency_contact_phone">
                    </div>
                </div>
                
            </div>
            <div style="text-align:right; margin-top: 2rem">
                <button type="submit" class="btn btn-primary" >Update</button>
          </div>
        </form>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'Register',
    data() {
        return {
            current_volunteer_info: { //use axios to call current information connected to current user
                first_name: 'John',
                last_name: 'Smith',
                phone:  '1234567890',
                email: 'name@example.com',
                emergency_contact_fname: 'Jane',
                emergency_contact_lname: 'Doe',
                emergency_contact_phone: '0987654321',


            },
            new_volunteer_info: {
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
            //call axios to update database with new_volunteer_info information
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
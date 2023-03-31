<template>
    <div class="container"> 
        <h3>Volunteer</h3>
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.first_name">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.last_name">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="phoneNumber" maxlength="14">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Email</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.email">
                    </div>
                    <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Address Line 1</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.address_line_1">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Address Line 2</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.address_line_2">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">City</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.city">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">State</label>
                        <div>
                            <div>
                            <select class="form-select" v-model="volunteer_info.state_id">
                                <option value="">Select a state</option>
                                <option v-for="state in filteredStates" :key="state.id" :value="state.id">{{ state.name }}</option>
                            </select>
                            </div>
                        </div>
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Zip</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.zip">
                    </div>
                </div>
                </div>
            </div>
            <br>
            <h3> Emergency Contact</h3>
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter First Name" v-model="volunteer_info.emergency_contact_fname">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter Last Name" v-model="volunteer_info.emergency_contact_lname">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter Phone Number" v-model="emergencyPhoneNumber" maxlength="14">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Relationship</label>
                        <div>
                            <div>
                            <select class="form-select" v-model="volunteer_info.rel_id">
                                <option value="">Relationship</option>
                                <option v-for="relationship in filteredRelationships" :key="relationship.id" :value="relationship.id">{{ relationship.name }}</option>
                            </select>
                            </div>
                        </div>
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
import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore.js'
import axios from "axios";
export default {
    name: 'Register',
    data() {
        return {
            msg:"Update Volunteer",
            volunteer_info: { //use axios to call current information connected to current user
                volunteer_id: 2,
                first_name: 'John',
                last_name: 'Smith',
                phone:  useVolunteerPhoneStore().volunteerPhone,
                email: 'name@example.com',
                emergency_contact_fname: 'Jane',
                emergency_contact_lname: 'Doe',
                emergency_contact_phone: '0987654321',
                address_line_1:'1234 Canal St',
                address_line_2:'Box 12',
                city:'Houston',
                state_id:'',
                zip: 12345,
                rel_id:''         
            },
            phoneNumber: useVolunteerPhoneStore().volunteerPhone,
            emergencyPhoneNumber: '0987654321',
            searchQuery: '',
            states: [
                { name: 'Alabama', id: 1 },
                { name: 'Alaska', id: 2 },
                { name: 'Arizona', id: 3 },
                { name: 'Arkansas', id: 4 },
                { name: 'California', id: 5 },
                { name: 'Colorado', id: 6 },
                { name: 'Connecticut', id: 7 },
                { name: 'Delaware', id: 8 },
                { name: 'District of Columbia', id: 9 },
                { name: 'Florida', id: 10 },
                { name: 'Georgia', id: 11 },
                { name: 'Hawaii', id: 12 },
                { name: 'Idaho', id: 13 },
                { name: 'Illinois', id: 14 },
                { name: 'Indiana', id: 15 },
                { name: 'Iowa', id: 16 },
                { name: 'Kansas', id: 17 },
                { name: 'Kentucky', id: 18 },
                { name: 'Louisiana', id: 19 },
                { name: 'Maine', id: 20 },
                { name: 'Maryland', id: 21 },
                { name: 'Massachusetts', id: 22 },
                { name: 'Michigan', id: 23 },
                { name: 'Minnesota', id: 24 },
                { name: 'Mississippi', id: 25 },
                { name: 'Missouri', id: 26 },
                { name: 'Montana', id: 27 },
                { name: 'Nebraska', id: 28 },
                { name: 'Nevada', id: 29 },
                { name: 'New Hampshire', id: 30 },
                { name: 'New Jersey', id: 31 },
                { name: 'New Mexico', id: 32 },
                { name: 'New York', id: 33 },
                { name: 'North Carolina', id: 34 },
                { name: 'North Dakota', id: 35 },
                { name: 'Ohio', id: 36 },
                { name: 'Oklahoma', id: 37 },
                { name: 'Oregon', id: 38 },
                { name: 'Pennsylvania', id: 39 },
                { name: 'Rhode Island', id: 40 },
                { name: 'South Carolina', id: 41 },
                { name: 'South Dakota', id: 42 },
                { name: 'Tennessee', id: 43 },
                { name: 'Texas', id: 44 },
                { name: 'Utah', id: 45 },
                { name: 'Vermont', id: 46 },
                { name: 'Virginia', id: 47 },
                { name: 'Washington', id: 48 },
                { name: 'West Virginia', id: 49 },
                { name: 'Wisconsin', id: 50 },
                { name: 'Wyoming', id: 51 }
            ],
            relationships: [
                {name: 'Parent', id: 1},
                {name: 'Child', id: 2},
                {name: 'Sibling', id: 3},
                {name: 'Family', id: 4},
                {name: 'Friend', id: 5},
                {name: 'Spouse', id: 6},
                {name: 'Partner', id: 7},
                {name: 'Acquiantance', id: 8},
                {name: 'Other', id: 9}
            ]
        };
    },
    watch: {
      phoneNumber(newValue) {
        this.formatPhoneNumber(newValue);
      },
      emergencyPhoneNumber(newValue) {
        console.log('wah')
        this.formatEmergencyPhoneNumber(newValue);
      }
    },
    computed: {
        filteredStates() {
            return this.states.filter(state => {
                return state.name.toLowerCase().includes(this.searchQuery.toLowerCase());
            });
        },
        filteredRelationships() {
            return this.relationships.filter(relationship => {
                return relationship.name.toLowerCase().includes(this.searchQuery.toLowerCase());
            });
        },
    },
    methods: {
        formatPhoneNumber(value) {
            if (!value) return value;
            const phoneNumber = value.replace(/[^\d]/g, '');
            const phoneNumberLength = phoneNumber.length;
            console.log('phoneNumberLength:', phoneNumberLength)
            if (phoneNumberLength > 0) {
                this.phoneNumber = this.phoneNumber
            }        
            if (phoneNumberLength == 1) {
                this.phoneNumber = this.phoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 2) {
                this.phoneNumber = this.phoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 3) {
                this.phoneNumber = this.phoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength > 3) {
                this.phoneNumber = `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
            }
            if (phoneNumberLength > 6){
                this.phoneNumber = `(${phoneNumber.slice(0,3)}) ${phoneNumber.slice(
                3,
                6,
                )}-${phoneNumber.slice(6, 10)}`;
            }
        },
        formatEmergencyPhoneNumber(value) {
            if (!value) return value;
            const phoneNumber = value.replace(/[^\d]/g, '');
            const phoneNumberLength = phoneNumber.length;
            console.log('phoneNumberLength:', phoneNumberLength)
            if (phoneNumberLength > 0) {
                this.emergencyPhoneNumber = this.emergencyPhoneNumber
            }
            if (phoneNumberLength == 1) {
                this.emergencyPhoneNumber = this.emergencyPhoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 2) {
                this.emergencyPhoneNumber = this.emergencyPhoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 3) {
                this.emergencyPhoneNumber = this.emergencyPhoneNumber.replace(/[^\d]/g, '');
            }
            if (phoneNumberLength > 3) {
                this.emergencyPhoneNumber = `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
            }
            if (phoneNumberLength > 6){
                this.emergencyPhoneNumber = `(${phoneNumber.slice(0,3)}) ${phoneNumber.slice(
                3,
                6,
                )}-${phoneNumber.slice(6, 10)}`;
            }
        },
        submitForm() {
            console.log('form submitted')
            this.phoneNumber = this.phoneNumber.replace(/[^\d]/g, '');
            this.emergencyPhoneNumber = this.emergencyPhoneNumber.replace(/[^\d]/g, '');
            this.volunteer_info.phone = this.phoneNumber
            this.volunteer_info.emergency_contact_phone = this.emergencyPhoneNumber
            console.log('this.volunteer_info.phone', this.volunteer_info.phone)
            console.log('this.phoneNumber:', this.phoneNumber)
            axios
            .post('http://127.0.0.1:5000/update_volunteer', this.volunteer_info)
            .then(() =>{
                this.volunteer_info={}
                alert('Volunteer Updated')
                this.$router.push('/profile/update')
            })
            .catch((error)=>{
                console.log(error);
            });
    }
}}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}
</style>
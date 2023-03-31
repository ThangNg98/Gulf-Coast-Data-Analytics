<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <h3> Volunteer</h3>
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
                        <input type="text" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.phone">
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
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Enter Phone Number" v-model="volunteer_info.emergency_contact_phone">
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
                <button type="submit" class="btn btn-primary" >Register</button>
          </div>
        </form>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'Register',
    data() {
        return {
            msg : "Volunteer Registration Form",
            volunteer_info: {
                first_name: '',
                last_name: '',
                phone:  '',
                email: '',
                emergency_contact_fname: '',
                emergency_contact_lname: '',
                emergency_contact_phone: '',
                address_line_1:'1234 Canal St',
                address_line_2:'Box 12',
                city:'Houston',
                state_id:'',
                date_created: this.getDate(),//new Date().toJSON("en-US", {timeZone: "America/Chicago"}).slice(0,10),
                volunteer_status_id: '2',
                zip: 12345,
                rel_id:'' ,
                waiver_signed: '2',
                zip: ''
            },
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
        submitForm() {
            //this.getDate();
            console.log("submit " + this.date_created);
            //console.log(new Date().toJSON("en-US", {timeZone: "America/Chicago"}).slice(0,10));
            axios
                .post('http://127.0.0.1:5000/add_volunteer', this.volunteer_info)
                .then(response => {
                    if (response.data == '1') {
                        alert('Volunteer with this phone number already exists.')
                    }
                    else {
                        this.volunteer_info = {}
                        alert('Registration Successful')
                        this.$router.push('/')

                    }
                })
                .catch((error) => {
                    console.log(error);
          });

        },
        getDate() {
            var today = new Date();
            today.setHours( today.getHours()+(today.getTimezoneOffset()/-60) );
            today = today.toJSON().slice(0, 10);
            return today;
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
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
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/volunteers"> Back to Volunteers</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" @click="updateButtonClicked = true">Update </button>
                <button type="submit" class="btn btn-danger"  @click="deleteButtonClicked = true">Delete</button>
            </div>
        </form>
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="clo">Waiver Signed</th>
                        <th scope="col">Waiver Signed Date</th>
                        <th scope="col">Total Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <input type="checkbox" v-model="waiverSigned">
                            </td>
                            <td>
                                <input type="date" id="date" v-model="volunteer_info.date_waiver_signed" @input="formatDate">
                            </td>
                            <td>[hours]</td>
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
    name: 'Register',
    data() {
        return {
            msg:"Update Volunteer",
            volunteer_info: { //use axios to call current information connected to current user
                volunteer_id:'',
                first_name: '',
                last_name: '',
                phone:  '',
                email: '',
                emergency_contact_fname: '',
                emergency_contact_lname: '',
                emergency_contact_phone: '',
                address_line_1:'',
                address_line_2:'',
                city:'',
                state_id:'',
                zip: '',
                rel_id:'',
                waiver_signed: '',
                date_waiver_signed: '' ,
                total_hours: ''              
            },
            updateButtonClicked: false,
            deleteButtonClicked: false,
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
        waiverSigned: {
            get() {
                return this.volunteer_info.waiver_signed == 1;
            },
            set(value) {
                this.volunteer_info.waiver_signed = value ? 1 : 2;
            }
        },
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
            if (this.updateButtonClicked == true) {
                this.updateButtonClicked = false
                if (!this.volunteer_info.date_waiver_signed) {
                    console.log('volunteer_info.date_waiver_signed does not have stuff in it')
                    this.volunteer_info.date_waiver_signed = null
                }
                axios
                .post('http://127.0.0.1:5000/admin_update_volunteer', this.volunteer_info)
                .then(() =>{
                    console.log(this.volunteer_info.date_waiver_signed)
                    this.volunteer_info={}
                    alert('Volunteer Updated')
                    this.$router.push('/admin/volunteers')
                    
                })
                .catch((error)=>{
                    console.log(error);
                });
            }
            else if (this.deleteButtonClicked = true) {
                this.deleteButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/delete_volunteer', this.volunteer_info)
                .then(() =>{
                    this.volunteer_info={}
                    alert('Volunteer Deleted')
                    this.$router.push('/admin/volunteers')
                })
            }
        },
        formatDate(event) {
            const date = new Date(event.target.value)
            const formattedDate = date.toISOString().slice(0, 10)
            this.date = formattedDate
        }
    },
    created() {
        axios.get(`http://127.0.0.1:5000/get_volunteer/${this.$route.params.volunteer_id}`).then(response => {
            console.log('response.data[0].date_waiver_signed: ', response.data[0].date_waiver_signed)
            if (response.data[0].date_waiver_signed == null) {
                console.log('date_waiver_signed is null')
                this.volunteer_info = response.data[0]
                this.volunteer_info.date_waiver_signed = ''
            }
            else {
                console.log('date_waiver_signed is not null')
                // parse the date string and format it in 'YYYY-MM-DD' format
                this.volunteer_info = response.data[0]
                this.volunteer_info.date_waiver_signed = new Date(this.volunteer_info.date_waiver_signed).toISOString().slice(0, 10);
            }
        })
    },
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto
}
</style>
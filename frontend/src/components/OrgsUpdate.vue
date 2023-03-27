<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Organization Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="organization.org_name">
                <label for="exampleFormControlInput1" class="form-label"> Address Line 1 </label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="organization.address_line_1">
                <label for="exampleFormControlInput1" class="form-label"> Address Line 2 </label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="organization.address_line_2">
                <label for="exampleFormControlInput1" class="form-label"> City </label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="organization.city">
                <label for="exampleFormControlInput1" class="form-label"> State </label>
                <div>
                    <select class="form-select"  v-model="organization.state_id">
                    <option value="">Select a state</option>
                    <option v-for="state in states" :key="state.id" :value="state.id">{{ state.name }}</option>
                    </select>
                </div>
                <label for="exampleFormControlInput1" class="form-label"> Zip </label>
                <input type="text" class="form-control" id="exampleFormControlInput1" v-model="organization.zip">
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/orgs"> Back to Organizations</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem"  @click="updateButtonClicked = true">Update </button>
                <button type="submit" class="btn btn-danger"  @click="deleteButtonClicked = true">Delete</button>
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
    name: 'OrgsUpdate',
    data() {
        return {
            msg : "Update Organization",
            organization: {
                org_id: 2,
                org_name: 'a BRAND NEW org',
                address_line_1: 'A BRAND NEW address',
                address_line_2: "A Second BRAND NEW address",
                city: 'NEW city',
                state_id: '',
                zip: '11111',
                org_status_id: 1
                
            },
            updateButtonClicked: false,
            deleteButtonClicked: false,
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
                ]
        };
    },
    methods: {
        submitForm() {
            if (this.updateButtonClicked == true) {
                this.updateButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/update_organization', this.organization)
                .then(() =>{
                    this.organization={}
                    alert('Organization Updated')
                    this.$router.push('/admin/orgs')
                })
                .catch((error)=>{
                    console.log(error);
                });
            }
            else if (this.deleteButtonClicked == true) {
                this.deleteButtonClicked = false
                axios
                .post('http://127.0.0.1:5000/delete_organization', this.organization)
                .then(() =>{
                    this.organization={}
                    alert('Organization Deleted')
                    this.$router.push('/admin/orgs')
                })
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
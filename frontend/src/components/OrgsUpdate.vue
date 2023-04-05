<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <div style="margin-top: 1rem; font-weight: bold">
                    * Required
                </div>
                <label for="orgName" class="form-label">Organization Name *</label>
                <input type="text" class="form-control" ref="orgName" v-model="organization.org_name" :class="{ 'is-invalid': errors.orgName }" :maxlength="50" :disabled="this.confirmModal">
                <div class="invalid-feedback">{{errors.orgName}}</div>

                <label for="address" class="form-label"> Address Line 1 *</label>
                <input type="text" class="form-control" ref="address" v-model="organization.address_line_1" :class="{ 'is-invalid': errors.address }" :maxlength="255" :disabled="this.confirmModal">
                <div class="invalid-feedback">{{errors.address}}</div>

                <label for="address2" class="form-label"> Address Line 2 </label>
                <input type="text" class="form-control" ref="address2" v-model="organization.address_line_2" :disabled="this.confirmModal">

                <label for="city" class="form-label"> City *</label>
                <input type="text" class="form-control" ref="city" v-model="organization.city" :class="{ 'is-invalid': errors.city }" :maxlength="60" :disabled="this.confirmModal">
                <div class="invalid-feedback">{{errors.city}}</div>

                <label for="state_select" class="form-label"> State *</label>
                <div>
                    <select class="form-select" ref="state_select" v-model="organization.state_id" :class="{ 'is-invalid': errors.state }" :disabled="this.confirmModal">
                    <option value="">Select a state</option>
                    <option v-for="state in states" :key="state.id" :value="state.id">{{ state.name }}</option>
                    </select>
                    <div class="invalid-feedback">{{errors.state}}</div>
                </div>
                <label for="zip" class="form-label"> Zip *</label>
                <input type="text" class="form-control" ref="zip" v-model="organization.zip" :class="{ 'is-invalid': errors.zip }" :maxlength="5" :disabled="this.confirmModal">
                <div class="invalid-feedback">{{errors.zip}}</div>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" :disabled="this.confirmModal"> <router-link class="nav-link" to="/admin/orgs"> Back to Organizations</router-link></button>
                <button type="submit" class="btn btn-danger" style="margin-right:0.5rem" @click="deleteButtonClicked = true" :disabled="this.confirmModal">Delete</button>
                <button type="submit" class="btn btn-primary" @click="updateButtonClicked = true" :disabled="this.confirmModal">Update </button>
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

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    </main>
</template>

<script>
import axios from "axios";
import ConfirmModal from './ConfirmModal.vue'
export default {
    name: 'OrgsUpdate',
    components: {
        ConfirmModal
    },
    data() {
        return {
            msg : "Update Organization",
            organization: {
                org_id: '',
                org_name: '',
                address_line_1: '',
                address_line_2: '',
                city: '',
                state_id: '',
                zip: '',
                org_status_id: ''
                
            },
            hours: null,
            num_volunteers: 0,
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
            ],
            errors: {},
            submitPressed: false,
            confirmModal: false
        };
    },
    watch: {
        'organization.org_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('orgName')
                } else {
                    this.addValidationStyle('orgName', 'Organization name is required.')
                }
            }
        },
        'organization.address_line_1'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('address')
                } else {
                    this.addValidationStyle('address', 'Address is required.')
                }
            }
        },
        'organization.city'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('city')
                } else {
                    this.addValidationStyle('city', 'City is required.')
                }
            }
        },
        'organization.state_id'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('state')
                } else {
                    this.addValidationStyle('state', 'State is required.')
                }
            }
        },
        'org_info.zip'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('zip')
                } else {
                    this.addValidationStyle('zip', 'Zip code is required.')
                }
            }
        }
    },
    created() {
        axios.get(`http://127.0.0.1:5000/get_org/${this.$route.params.org_id}`).then(response => {
        this.organization.org_id = response.data[0].org_id;
        this.organization.org_name = response.data[0].org_name;
        this.organization.address_line_1 = response.data[0].address_line_1;
        this.organization.address_line_2 = response.data[0].address_line_2;
        this.organization.city = response.data[0].city;
        this.organization.state_id = response.data[0].state_id;
        this.organization.zip = response.data[0].zip;
        this.organization.org_status_id = response.data[0].org_status_id;
        this.hours = response.data[0].total_hours;
        this.num_volunteers = response.data[0].num_volunteers
        })
    },
    methods: {
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        closeConfirmModal(value) {
            this.confirmModal = false;
            console.log(value)
            if (value === 'yes') {
                if (this.title === 'Please Confirm Update') {
                    console.log('update confirm')
                    this.title = '';
                    this.message = '';
                    axios
                    .post('http://127.0.0.1:5000/update_organization', this.organization)
                    .then(() =>{
                        this.organization={}
                        this.$router.push('/admin/orgs?update=true')
                    })
                    .catch((error)=>{
                        console.log(error);
                    });
                }
                else if (this.title === 'Please Confirm Delete') {
                    console.log('delete confirm')
                    this.title = '';
                    this.message = '';
                    axios
                    .post('http://127.0.0.1:5000/delete_organization', this.organization)
                    .then(() =>{
                        this.organization={}
                        this.$router.push('/admin/orgs?delete=true')
                    })
                }
            }
        },
        submitForm() {

            this.submitPressed = true

            this.errors = {}

            if (!this.organization.org_name) {
                this.errors.orgName = "Organization name is required."
            }
            if (!this.organization.address_line_1) {
                this.errors.address = 'Address is required.'
            }
            if (!this.organization.city) {
                this.errors.city = 'City is required.'
            }
            if (!this.organization.state_id) {
                this.errors.state = 'State is required.'
            }
            if (!this.organization.zip) {
                this.errors.zip = 'Zip code is required.'
            }
            if (this.organization.zip) {
                if (!/^\d+$/.test(this.organization.zip)) {
                    this.errors.zip = 'Zip code must be digits only.'
                }
                else if (this.organization.zip.length !== 5) {
                    this.errors.zip = 'Zip code must be 5 digits in length.'
                }
            }
            if (Object.keys(this.errors).length === 0) {
                if (this.updateButtonClicked == true) {
                    console.log('update clicked')
                    this.updateButtonClicked = false
                    this.confirmModal = true
                    this.title = 'Please Confirm Update'
                    this.message = "Are you sure you want to update this organization?"
                }
                else if (this.deleteButtonClicked == true) {
                    console.log('delete clicked')
                    this.deleteButtonClicked = false
                    this.confirmModal = true
                    this.title = 'Please Confirm Delete'
                    this.message = "Are you sure you want to delete this organization?"
                }
            }
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
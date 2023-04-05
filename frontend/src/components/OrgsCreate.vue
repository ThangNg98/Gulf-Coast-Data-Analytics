<template>
    <main>
        <div>
            <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem">{{ msg }}</h1>
        </div>
        <div class="container"> 
            <form @submit.prevent="submitForm">
                <div>
                    <div style="margin-top: 1rem; font-weight: bold">
                    * Required
                    </div>
                    <label for="orgName" class="form-label">Organization Name *</label>
                    <input type="text" class="form-control" ref="orgName" v-model="org_info.org_name" :class="{ 'is-invalid': errors.orgName }" :maxlength="50" :disabled="confirmModal">
                    <div class="invalid-feedback">{{errors.orgName}}</div>

                    <label for="address" class="form-label"> Address Line 1 *</label>
                    <input type="text" class="form-control" ref="address" v-model="org_info.address_line_1" :class="{ 'is-invalid': errors.address }" :maxlength="255" :disabled="confirmModal">
                    <div class="invalid-feedback">{{errors.address}}</div>

                    <label for="address2" class="form-label"> Address Line 2</label>
                    <input type="text" class="form-control" ref="address2" v-model="org_info.address_line_2" :disabled="confirmModal">

                    <label for="city" class="form-label"> City *</label>
                    <input type="text" class="form-control" ref="city" v-model="org_info.city" :class="{ 'is-invalid': errors.city }" :maxlength="60" :disabled="confirmModal">
                    <div class="invalid-feedback">{{errors.city}}</div>

                    <div>
                        <label for="state_select" class="form-label">State *</label>
                        <select class="form-select" id="state_select" v-model="org_info.state_id" :class="{ 'is-invalid': errors.state }" :disabled="confirmModal">
                            <option value="">Select a state</option>
                            <option v-for="state in filteredStates" :key="state.id" :value="state.id">{{ state.name }}</option>
                        </select>
                        <div class="invalid-feedback">{{errors.state}}</div>
                    </div>

                    <label for="exampleFormControlInput1" class="form-label"> Zip *</label>
                    <input type="text" class="form-control" id="exampleFormControlInput1" v-model="org_info.zip" :class="{ 'is-invalid': errors.zip }" :maxlength="5" :disabled="confirmModal">
                    <div class="invalid-feedback">{{errors.zip}}</div>

                </div>
                <br>
                <div style="text-align:right; margin-top: 2rem;">
                    <button type="button" class="btn btn-success" style="margin-right:0.5rem; text-align:left" :disabled="confirmModal">
                        <router-link class="nav-link" to="/admin/orgs" > Back to Organizations</router-link>
                    </button>
                    <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" :disabled="confirmModal">Submit</button>
                </div>
            </form>
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
    name: 'OrgsCreate',
    components: {
        ConfirmModal
    },
    data() {
        return {
            msg : "Add New Organization",
            org_info : {
                org_name: '',
                address_line_1: '',
                address_line_2: '',
                city: '',
                state_id: '',
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
            confirmModal: false,
            title: '',
            message: '',
            errors: {},
            submitPressed: false,
        };
    },
    watch: {
        'org_info.org_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('orgName')
                } else {
                    this.addValidationStyle('orgName', 'Organization name is required.')
                }
            }
        },
        'org_info.address_line_1'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('address')
                } else {
                    this.addValidationStyle('address', 'Address is required.')
                }
            }
        },
        'org_info.city'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('city')
                } else {
                    this.addValidationStyle('city', 'City is required.')
                }
            }
        },
        'org_info.state_id'(newValue, oldValue) {
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
    computed: {
        filteredStates() {
            return this.states.filter(state => {
                return state.name.toLowerCase().includes(this.searchQuery.toLowerCase());
            });
        }
    },
    methods: {
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        closeConfirmModal(value) {
            this.confirmModal = false
            this.title = ''
            this.message = ''
            console.log(value)
            if (value === 'yes') {
                axios
                .post('http://127.0.0.1:5000/create_organization', this.org_info)
                .then(() =>{
                    this.org_info={}
                    this.$router.push('/admin/orgs?success=true')
                })
                .catch((error)=>{
                    console.log(error);
                });
            }
        },
        submitForm() {
            this.submitPressed = true

            this.errors = {}

            if (!this.org_info.org_name) {
                this.errors.orgName = 'Organization name is required.'
            }
            if (!this.org_info.address_line_1) {
                this.errors.address = 'Address is required.'
            }
            if (!this.org_info.city) {
                this.errors.city = 'City is required.'
            }
            if (!this.org_info.state_id) {
                this.errors.state = 'State is required.'
            }
            if (!this.org_info.zip) {
                this.errors.zip = 'Zip code is required.'
            }
            if (this.org_info.zip) {
                if (!/^\d+$/.test(this.org_info.zip)) {
                    this.errors.zip = 'Zip code must be digits only.'
                }
                else if (this.org_info.zip.length !== 5) {
                    this.errors.zip = 'Zip code must be 5 digits in length.'
                }
            }
            if (Object.keys(this.errors).length === 0) {
                // Submit form
                this.confirmModal = true
                this.title = 'Please Confirm Creation'
                this.message = 'Are you sure you want to create this organization?'
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
<template>
    <div class="container" style="text-align:left"> 
        <div class="text-danger" style="margin-top: 1rem; font-weight: bold">
            * Required
        </div>
        <h3>Volunteer</h3>
        <form @submit.prevent="submitForm">
            <div>
                <div class="row">
                    <div class="col-6"> 
                        <label for="volFirstName" class="form-label">First Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volFirstName" v-model="volunteer_info.first_name" :class="{ 'is-invalid': errors.volFirstName }" :maxlength="50" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volFirstName}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-8"> 
                        <label for="volLastName" class="form-label">Last Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volLastName" v-model="volunteer_info.last_name" :class="{ 'is-invalid': errors.volLastName }" :maxlength="50" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volLastName}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6"> 
                        <label for="volPhone" class="form-label">Phone Number <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volPhone" v-model="volunteer_info.phone" :class="{ 'is-invalid': errors.volPhone }" :maxlength="14" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volPhone}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Email</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" v-model="volunteer_info.email" :disabled="confirmModal">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="volAddress" class="form-label">Address Line 1 <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volAddress" v-model="volunteer_info.address_line_1"  :class="{ 'is-invalid': errors.volAddress }" :maxlength="255" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volAddress}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="volAddress2" class="form-label">Address Line 2</label>
                        <input type="text" class="form-control" ref="volAddress2" v-model="volunteer_info.address_line_2" :disabled="confirmModal">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="volCity" class="form-label">City <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volCity" v-model="volunteer_info.city" :class="{ 'is-invalid': errors.volCity }" :maxlength="60" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volCity}}</div>
                    </div>
                    <div class="col"> 
                        <label for="volState" class="form-label">State <span class="text-danger">*</span></label>
                        <div>
                            <div>
                            <select class="form-select" ref="volState" v-model="volunteer_info.state_id" :class="{ 'is-invalid': errors.volState }" :disabled="confirmModal">
                                <option value="">Select a state</option>
                                <option v-for="state in filteredStates" :key="state.id" :value="state.id">{{ state.name }}</option>
                            </select>
                            <div class="invalid-feedback">{{errors.volState}}</div>
                            </div>
                        </div>
                    </div>
                    <div class="col"> 
                        <label for="volZip" class="form-label">Zip <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="volZip" v-model="volunteer_info.zip" :class="{ 'is-invalid': errors.volZip }" :maxlength="5" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.volZip}}</div>
                    </div>
                </div>
            </div>
            <br>
            <h3> Emergency Contact</h3>
            <div>
                <div class="row">
                    <div class="col-6"> 
                        <label for="emFirstName" class="form-label">First Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="emFirstName" v-model="volunteer_info.emergency_contact_fname" :class="{ 'is-invalid': errors.emFirstName }" :maxlength="45" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.emFirstName}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-8"> 
                        <label for="emLastName" class="form-label">Last Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="emLastName" v-model="volunteer_info.emergency_contact_lname" :class="{ 'is-invalid': errors.emLastName }" :maxlength="45" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.emLastName}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6"> 
                        <label for="emPhone" class="form-label">Phone Number <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" ref="emPhone" v-model="volunteer_info.emergency_contact_phone" :class="{ 'is-invalid': errors.emPhone }" :maxlength="14" :disabled="confirmModal">
                        <div class="invalid-feedback">{{errors.emPhone}}</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-9"> 
                        <label for="emRel" class="form-label">Relationship</label>
                        <div>
                            <div>
                            <select class="form-select" ref="emRel" v-model="volunteer_info.rel_id" :class="{ 'is-invalid': errors.emRel }" :disabled="confirmModal">
                                <option value="">Select a Relationship</option>
                                <option v-for="relationship in filteredRelationships" :key="relationship.id" :value="relationship.id">{{ relationship.name }}</option>
                            </select>
                            <div class="invalid-feedback">{{errors.emRel}}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="text-align:right; margin-top: 2rem">
                <button type="submit" class="btn btn-primary" :disabled="confirmModal">Update</button>
          </div>
        </form>
    </div>

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

</template>

<script>
import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore.js'
import ConfirmModal from './ConfirmModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { getVolunteerIDAPI, getVolunteerAPI, updateVolunteerAPI } from '../api/api.js'
import axios from "axios";
export default {
    name: 'Register',
    components: {
        ConfirmModal,
        LoadingModal,        
    },
    data() {
        return {
            msg:"Update Volunteer",
            volunteer_info: {
                volunteer_id: null,
                first_name: null,
                last_name: null,
                phone:  null,
                email: null,
                emergency_contact_fname: null,
                emergency_contact_lname: null,
                emergency_contact_phone: null,
                address_line_1:null,
                address_line_2:null,
                city: null,
                state_id:'',
                zip: null,
                rel_id:''         
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
                {name: 'Acquaintance', id: 1},
                {name: 'Aunt', id: 2},
                {name: 'Child', id: 3},
                {name: 'Friend', id: 4},
                {name: 'Grandparent', id: 5},
                {name: 'Legal Guardian', id: 6},
                {name: 'Parent', id: 7},
                {name: 'Partner', id: 8},
                {name: 'Sibling', id: 9},
                {name: 'Spouse', id: 10},
                {name: 'Uncle', id: 11},
                {name: 'Other', id: 12}

            ],
            errors: {},
            submitPressed: false,
            confirmModal: false,
            title: '',
            message: '',
            isLoading: false,
        };
    },
    watch: {
        'volunteer_info.first_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volFirstName')
                } else {
                    this.addValidationStyle('volFirstName', 'First name is required.')
                }
            }
        },
        'volunteer_info.last_name'(newValue, oldValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volLastName')
                } else {
                    this.addValidationStyle('volLastName', 'Last name is required.')
                }
            }
        },
        'volunteer_info.phone'(newValue) {
            this.formatPhoneNumber(newValue, 'phone');
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volPhone')
                } else {
                    this.addValidationStyle('volPhone', 'Phone number is required.')
                }
            }
        },
        'volunteer_info.address__line_1'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volAddress')
                } else {
                    this.addValidationStyle('volAddress', 'Primary address is required.')
                }
            }
        },
        'volunteer_info.city'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volCity')
                } else {
                    this.addValidationStyle('volCity', 'City is required.')
                }
            }
        },
        'volunteer_info.state_id'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volState')
                } else {
                    this.addValidationStyle('volState', 'State is required.')
                }
            }
        },
        'volunteer_info.zip'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('volZip')
                } else {
                    this.addValidationStyle('volZip', 'Zip code is required.')
                }
            }
        },
        'volunteer_info.emergency_contact_fname'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('emFirstName')
                } else {
                    this.addValidationStyle('emFirstName', 'First name is required.')
                }
            }
        },
        'volunteer_info.emergency_contact_lname'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('emLastName')
                } else {
                    this.addValidationStyle('emLastName', 'Last name is required.')
                }
            }
        },
        'volunteer_info.emergency_contact_phone'(newValue) {
            this.formatPhoneNumber(newValue, 'emergency_contact_phone');
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('emPhone')
                } else {
                    this.addValidationStyle('emPhone', 'Phone number is required.')
                }
            }
        },
        'volunteer_info.rel_id'(newValue) {
            if (this.submitPressed) {
                if (newValue) {
                    this.removeValidationStyle('emRel')
                } else {
                    this.addValidationStyle('emRel', 'Relationship is required.')
                }
            }
        },
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
    mounted() {
        console.log('v_update profile mounted')
        this.loadData();
    },
    methods: {
        async loadData() {
            this.isLoading = true;
            try {
                await this.getVolunteerID();
                await this.getVolunteerData();
            } catch (error) {
                console.log(error)
            }
            this.isLoading = false;
        },
        async getVolunteerID() {
            const phone = useVolunteerPhoneStore().volunteerPhone
            console.log('phone:', phone)
            try {
                const response = await getVolunteerIDAPI(phone);
                this.volunteer_info.volunteer_id = response.data[0].volunteer_id
            } catch (error) {
                console.log(error)
            }
        },
        async getVolunteerData() {
            try {
                const response = await getVolunteerAPI(this.volunteer_info.volunteer_id)
                this.volunteer_info = response.data[0]
                console.log('this.volunteer info after getVolunteerData', this.volunteer_info)
            } catch (error) {
                console.log(error)
            }
        },
        removeValidationStyle(name) {
            this.errors[name] = null
        },
        addValidationStyle(name, des) {
            this.errors[name] = des
        },
        formatPhoneNumber(value, field) {
            console.log('field:', field)
            if (!value || typeof value !== 'string') {
                return value;
            }
            const phoneNumber = value.replace(/[^\d]/g, '');
            const phoneNumberLength = phoneNumber.length;
            console.log('phoneNumberLength:', phoneNumberLength)
            if (phoneNumberLength > 0) {
            this.volunteer_info[field] = this.volunteer_info[field]
            }        
            if (phoneNumberLength == 1) {
            this.volunteer_info[field] = this.volunteer_info[field].replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 2) {
            this.volunteer_info[field] = this.volunteer_info[field].replace(/[^\d]/g, '');
            }
            if (phoneNumberLength == 3) {
            this.volunteer_info[field] = this.volunteer_info[field].replace(/[^\d]/g, '');
            }
            if (phoneNumberLength > 3) {
            this.volunteer_info[field] = `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
            }
            if (phoneNumberLength > 6){
            this.volunteer_info[field] = `(${phoneNumber.slice(0,3)}) ${phoneNumber.slice(
            3,
            6,
            )}-${phoneNumber.slice(6, 10)}`;
            }
        },
        closeConfirmModal(value) {
            this.confirmModal = false;
            if (value === 'yes') {
                this.title = '';
                this.message = '';
                this.volunteer_info.phone = this.volunteer_info.phone.replace(/[^\d]/g, '');
                console.log('LOOK HERE this.volunteer_info.phone', this.volunteer_info.phone)
                this.volunteer_info.emergency_contact_phone = this.volunteer_info.emergency_contact_phone.replace(/[^\d]/g, '');
                this.updateVolunteer();
                // axios
                // .post('http://127.0.0.1:5000/update_volunteer', this.volunteer_info)
                // .then(() =>{
                //     this.volunteer_info.phone = this.volunteer_info.phone.replace(/[^\d]/g, '');
                //     useVolunteerPhoneStore().setVolunteerPhone(this.volunteer_info.phone, this.volunteer_info.volunteer_id, this.volunteer_info.first_name)
                //     console.log('useVolunteerPhoneStore.volunteerPhone', useVolunteerPhoneStore().volunteerPhone)
                //     this.$router.push('/profile/history?update=true')
                // })
                // .catch((error)=>{
                //     console.log(error);
                // });
            }
        },
        async updateVolunteer() {
            try {
                await updateVolunteerAPI(this.volunteer_info);
                this.volunteer_info.phone = this.volunteer_info.phone.replace(/[^\d]/g, '');
                useVolunteerPhoneStore().setVolunteerPhone(
                    this.volunteer_info.phone, 
                    this.volunteer_info.volunteer_id, 
                    this.volunteer_info.first_name
                );
                this.$router.push('/profile/history?update=true');
            } catch (error) {
                console.log(error)
            }
        },
        submitForm() {
            console.log('submit form')
            this.submitPressed = true
            this.errors = {}
            if (!this.volunteer_info.first_name) {
                this.errors.volFirstName = "First name is required."
            }
            if (!this.volunteer_info.last_name) {
                this.errors.volLastName = "Last name is required."
            }
            if (!this.volunteer_info.phone) {
                this.errors.volPhone = "Phone number is required."
            }
            else if (this.volunteer_info.phone) {
                const phoneNumberRegex = /^\d{10}$/
                const phoneNumberDigitsOnly = this.volunteer_info.phone.replace(/[^\d]/g, '');
                if (!/^\d+$/.test(phoneNumberDigitsOnly)) {
                    this.errors.volPhone = 'Phone number must be digits only.'
                }
                else if (phoneNumberDigitsOnly.length !== 10) {
                    this.errors.volPhone = 'Phone number must be 10 digits in length.'
                }
            }
            if (!this.volunteer_info.address_line_1) {
                this.errors.volAddress = "Primary address is required."
            }
            if (!this.volunteer_info.city) {
                this.errors.volCity = "City is required."
            }
            if (!this.volunteer_info.state_id) {
                this.errors.volState = "State is required."
            }
            if (!this.volunteer_info.zip) {
                this.errors.volZip = 'Zip code is required.'
            }
            if (this.volunteer_info.zip) {
                if (!/^\d+$/.test(this.volunteer_info.zip)) {
                    this.errors.volZip = 'Zip code must be digits only.'
                }
                else if (this.volunteer_info.zip.length !== 5) {
                    this.errors.volZip = 'Zip code must be 5 digits in length.'
                }
            }
            if (!this.volunteer_info.emergency_contact_fname) {
                this.errors.emFirstName = 'First name is required.'
            }
            if (!this.volunteer_info.emergency_contact_lname) {
                this.errors.emLastName = 'Last name is required.'
            }
            if (!this.volunteer_info.emergency_contact_phone) {
                this.errors.emPhone = "Phone number is required."
            }
            else if (this.volunteer_info.emergency_contact_phone) {
                const phoneNumberRegex = /^\d{10}$/
                const phoneNumberDigitsOnly = this.volunteer_info.emergency_contact_phone.replace(/[^\d]/g, '');
                if (!/^\d+$/.test(phoneNumberDigitsOnly)) {
                    this.errors.emPhone = 'Phone number must be digits only.'
                }
                else if (phoneNumberDigitsOnly.length !== 10) {
                    this.errors.emPhone = 'Phone number must be 10 digits in length.'
                }
            }
            if (!this.volunteer_info.rel_id) {
                this.errors.emRel = 'Relationship is required.'
            }
            if (Object.keys(this.errors).length === 0) {
                this.confirmModal = true
                this.title = 'Please Confirm Update'
                this.message = "Are you sure you want to update your information?"
            }
    },
}}
</script>

<style scoped>
@media only screen and (min-width: 768px) {
    .container {
      margin: auto;
      padding-left: auto;
      padding-right: auto;
      width: 50%
    }
    }

@media only screen and (min-width: 992px) {
.container {
    margin: auto;
    padding-left: auto;
    padding-right: auto;
    width: 40%
}
}

@media only screen and (min-width: 1200px) {
.container {
    margin: auto;
    padding-left: auto;
    padding-right: auto;
    width: 35%
}
}
</style>
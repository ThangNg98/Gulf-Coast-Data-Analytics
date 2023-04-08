<template>
  <main>
    <div class="container">
      <div class="text-center mt-5">
        <h1>{{ msg }}</h1>
      </div>
      <!--Form for submitting phone number-->
      <form class="mt-5" @submit.prevent="handleSubmitForm">
        <!--Header-->
        <div class="form-group text-center">
          <h2>Enter Phone Number</h2>
          <!--If phone number input is not exactly 10 digits upon submit, this error message appears-->
          <div class="invalid-feedback" v-if="error">
            Phone number must be 10 digits.
          </div>
        </div>
        <!--Phone number input field-->
        <div class="form-group">
          <input type="tel" class="form-control mx-auto" required style="max-width: 300px" @keydown="reviewKey" v-model="phoneNumber" maxlength="14" >
        </div>
        <br>
        <!--Submit button-->
        <div class="text-center">
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>

    <Transition name="bounce">
        <ConfirmModal v-if="confirmModal" @close="closeConfirmModal" :title="title" :message="message"/>
    </Transition>

    <Transition name="bounce">
        <SuccessModal v-if="successModal" @close="closeSuccessModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <alert-modal v-if="showModal" @close="closeAlertModal" :title="title" :message="message" />
    </Transition>
    
    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

  </main>
</template>
  
<script>
  import axios from 'axios'  
  import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore'
  import SuccessModal from '../components/SuccessModal.vue'
  import ConfirmModal from '../components/ConfirmModal.vue'
  import LoadingModal from '../components/LoadingModal.vue'
  import AlertModal from '@/components/AlertModal.vue';
  import { useLoadingStore } from '../stores/LoadingStore'
  import { getPhoneListAPI } from '../api/api.js'

  export default {
    name: 'Home',
    components: {
      SuccessModal,
      ConfirmModal,
      LoadingModal,
      AlertModal,
    },
    data() {
      return {
        msg : "Welcome to The Living Legacy Center",
        //variable to hold the phoneNumber
        phoneNumber: null,
        //variable that represents an array of accepted keys. Input in the phone number field only occurs when one of these keys are pressed
        acceptedKeys: [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "Backspace",
          "Delete",
          "ArrowLeft",
          "ArrowRight",
          "Enter",
          "Shift",
          "Alt",
          "Home",
          "End"
        ],
        //variable that determines whether the error message shows
        error: false,
        volunteerPhoneList: [],
        successModal: false,
        confirmModal: false,
        showModal: false,
        title: '',
        message: '',
        isLoading: false,
      }
    },
    watch: {
      phoneNumber(newValue) {
        this.formatPhoneNumber(newValue);
      }
    },
    mounted() {
      console.log('mounted')
      const query = new URLSearchParams(this.$route.query);
      if (query.get('register') === 'true') {
          console.log('register is true')
          this.successModal = true;
          this.title = "You are registered!"
          this.message = "Please wait until you have been approved."
      }
      this.loadData();
      // axios
      //   .get('https://llc.onrender.com/volunteer_phone/')
      //   .then(response => {
      //     console.log('volunteer_phone response:', response)
      //     this.volunteerPhoneList = response.data;
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })
    },
    methods: {
      async loadData() {
        this.isLoading = true;
        try {
          const response = await getPhoneListAPI();
          this.volunteerPhoneList = response.data
        } catch (error) {
          console.log(error);
        }
        this.isLoading = false;
      },
      showAlertModal() {
      this.showModal = true;
      this.title = 'Login Failed';
      this.message = 'Please wait until you are approved by an administrator.';
      },
      closeAlertModal() {
        this.showModal = false;
        this.title = '';
        this.message = '';
      },
      closeSuccessModal() {
            this.successModal = false;
            this.title = '';
            this.message = '';
      },
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
      showConfirmModal() {
        this.confirmModal = true
        this.title = 'Phone Number Not Found'
        this.message = 'Would you like to register?'
      },
      closeConfirmModal(value) {
          this.confirmModal = false;
          if (value === 'yes') {
              this.title = '';
              this.message = '';
              this.$router.push({
                path: '/register',
                query: {
                  phoneNumber: this.phoneNumber
                }
              });
            }
      },
      //method called when form submits
      handleSubmitForm() {
        console.log('submit form')
        // error checking - if phone number is not exactly 10 digits, then error variable is set to true, revealing the error message
        const phoneNumberRegex = /^\d{10}$/

        this.phoneNumber = this.phoneNumber.replace(/[^\d]/g, '');
        console.log('this.phoneNumber:', this.phoneNumber)

        // input is 10 digits, form is submitted
        if (phoneNumberRegex.test(this.phoneNumber)) {
          this.error = false

          // check if phoneNumber is already in the volunteerPhoneList array
          const volunteer = this.volunteerPhoneList.find(v => v.phone === this.phoneNumber)

          if (volunteer) {
            console.log('Volunteer found in list')
            if (volunteer.waiver_signed == '2') {
              this.showAlertModal();
            } else if (volunteer.waiver_signed == '1') {
              console.log('setVolunteerPhone before: ', useVolunteerPhoneStore().volunteerPhone)
              console.log('setVolunteerID before: ', useVolunteerPhoneStore().volunteerID)
              useVolunteerPhoneStore().setVolunteerPhone(this.phoneNumber, volunteer.volunteer_id, volunteer.first_name)
              console.log('setVolunteerPhone after: ', useVolunteerPhoneStore().volunteerPhone)
              console.log('setVolunteerID after: ', useVolunteerPhoneStore().volunteerID)
              this.$router.push('/profile/checkin')
            }
          }
          else {
            console.log('Volunteer not found in list')
            this.showConfirmModal()
          }

        // input is not 10 digits, form is not submitted and error is revealed
        } 
        else {
          this.error = true
        }
      },
      // whenever a keydown event occurs, this checks which key was pressed. If it was anything other than what it is included in the acceptedKeys array, then the input is prevented
      reviewKey(e) {
        if (
          !(
            this.acceptedKeys.includes(e.key) ||
            (e.ctrlKey && (e.key === "c" || e.key === "v"))
          )
        ) {
          e.preventDefault();
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    max-width: 500px;
    margin: auto;
  }
  
  .form-control:focus {
    box-shadow: none;
  }
  
  .invalid-feedback {
    display: block;
    margin-top: 0.5rem;
    color: #dc3545;
  }
  
  .btn-primary {
    background-color: #3f51b5;
    border-color: #3f51b5;
  }
  
  .btn-primary:hover {
    background-color: #303f9f;
    border-color: #303f9f;
  }
  </style>
  
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
  </main>
</template>
  
<script>
  import axios from 'axios'  
  import { useVolunteerPhoneStore } from '@/stores/VolunteerPhoneStore'

  export default {
    name: 'Home',
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
      }
    },
    watch: {
      phoneNumber(newValue) {
        this.formatPhoneNumber(newValue);
      }
    },
    mounted() {
      axios
        .get('http://127.0.0.1:5000/volunteer_phone/')
        .then(response => {
          console.log('volunteer_phone response:', response)
          this.volunteerPhoneList = response.data;
        })
        .catch(error => {
          console.log(error);
        })
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
      //method called when form submits
      handleSubmitForm() {
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
            console.log('setVolunteerPhone before: ', useVolunteerPhoneStore().volunteerPhone)
            console.log('setVolunteerID before: ', useVolunteerPhoneStore().volunteerID)
            useVolunteerPhoneStore().setVolunteerPhone(this.phoneNumber, volunteer.volunteer_id)
            console.log('setVolunteerPhone after: ', useVolunteerPhoneStore().volunteerPhone)
            console.log('setVolunteerID after: ', useVolunteerPhoneStore().volunteerID)
            alert('Login Success')
            this.$router.push('/profile/checkin')
          }
          else {
            console.log('Volunteer not found in list')
            if (confirm("Phone number not found. Would you like to register?") == true) {
              this.$router.push('/register')
            } else {
              this.phoneNumber = "";
            }
            
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
  
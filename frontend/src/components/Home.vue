<template>
    <main>
      <div class="container">
        <div class="text-center mt-5">
          <h1>{{ msg }}</h1>
        </div>
        <form class="mt-5" @submit.prevent="handleSubmitForm">
          <div class="form-group text-center">
            <h2>Enter Phone Number</h2>
          </div>
          <div class="form-group">
            <input type="tel" class="form-control mx-auto" required style="max-width: 300px" @keydown="reviewKey" v-model="phoneNumber">
            <div class="invalid-feedback" v-if="error">
              Phone number must be 10 digits.
            </div>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </form>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    name: 'Home',
    data() {
      return {
        msg : "Welcome to The Living Legacy Center",
        phoneNumber: null,
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
          "Enter"
        ],
        error: false
      }
    },
    methods: {
      handleSubmitForm() {
        const phoneNumberRegex = /^\d{10}$/; // regular expression to match 10 digits
        if (phoneNumberRegex.test(this.phoneNumber)) {
          this.error = false
          alert('Submitted');
        } else {
          this.error = true
        }
      },
      reviewKey(e) {
        if (!this.acceptedKeys.includes(e.key)) {
          e.preventDefault()
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
  
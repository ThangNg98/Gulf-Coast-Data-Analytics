<template>
    <div class="login-page">
      <h1>Login</h1>
      <div class="phone-number-input">
        <div v-for="(digit, index) in 10" :key="index" class="digit-box">
          <input ref="digitInputs" type="text" maxlength="1" v-model="phoneNumber[index]" @keyup="focusNextInput(index, $event)" />
        </div>
      </div>
      <button class="submit-button" @click="submitPhoneNumber">Submit</button>
    </div>
    <p>phoneNumber: {{ phoneNumber }}</p>
</template>
  
  <script>
  export default {
    data() {
      return {
        phoneNumber: ['', '', '', '', '', '', '', '', '', ''],
      };
    },
    mounted() {
      if (this.phoneNumber.join('') === '') { // Check if phone number is empty
        this.$refs.digitInputs[0].focus(); // Focus on first digit box
      }
    },
    methods: {
      submitPhoneNumber() {
        const phoneNumberString = this.phoneNumber.join(''); // Concatenate digits into a string
        const phoneNumber = parseInt(phoneNumberString); // Convert string to number
        // Handle submit logic with phoneNumber here
        alert('Submitted')
      },
      focusNextInput(index, event) {
        if (event.keyCode >= 48 && event.keyCode <= 57) { // Check if key pressed is a digit
          const inputBox = this.$refs.digitInputs[index];
          if (inputBox.value === '') { // Check if input box is empty
            inputBox.value = event.key; // Replace contents with new digit
          } else if (index < 9) { // Check if not the last digit box
            inputBox.value = event.key; // Replace contents with new digit
            this.$refs.digitInputs[index + 1].focus(); // Focus on the next digit box
          } else {
            this.submitPhoneNumber(); // Submit the phone number if last digit box
          }
        } else if (event.keyCode === 8 && index > 0) { // Check if key pressed is backspace and not the first digit box
          this.$refs.digitInputs[index - 1].focus(); // Focus on the previous digit box
        }
      },
    },
    watch: {
      phoneNumber: {
        handler: function (val) {
          if (val.join('') === '') { // Check if phone number is empty
            this.$refs.digitInputs[0].focus(); // Focus on first digit box
          }
        },
        deep: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .login-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f2f2f2;
  }
  
  .phone-number-input {
    display: flex;
    align-items: center;
    justify-content: center;  
    margin: 20px 0;
  }
  
  .digit-box {
    border: 1px solid #cccccc;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    width: 40px;
    height: 40px;
    margin-right: 10px;
  }
  
  .digit-box input[type="text"] {
    border: none;
    font-size: 24px;
    text-align: center;
    width: 40px;
  }
  
  .submit-button {
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    cursor: pointer;
  }
    
  .submit-button:hover {
    background-color: #0062cc;
  }
  </style>
  
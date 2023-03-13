<template>
  <div class="login-page">
    <h1 class="my-element">Login</h1>
    <div class="phone-number-input">
      <div v-for="(digit, index) in 10" :key="index" class="input-group digit-box">
        <input
          ref="digitInputs"
          type="tel"
          pattern="[0-9]*"
          inputmode="numeric"
          v-model="phoneNumber[index]"
          @keydown="preventInput(index, $event)"
          class="form-control"
          aria-label="Phone number digit"
          @focus="activeInputIndex = index"
          autocomplete="nope"
        />
      </div>
      <div class="invalid-feedback">
        Please enter a valid phone number
      </div>
    </div>
    <div class="keypad-container large-keypad">
      <div class="keypad">
        <div class="row">
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('1')">1</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('2')">2</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('3')">3</button>
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('4')">4</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('5')">5</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('6')">6</button>
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('7')">7</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('8')">8</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit('9')">9</button>
          </div>
        </div>
        <div class="row">
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="clearDigits()">Clear</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="addDigit(0)">0</button>
          </div>
          <div class="col-4">
            <button class="btn btn-outline-primary key" @click="deleteDigit()">&lt;</button>
          </div>
        </div>
      </div>
    </div>
    <button class="btn btn-primary submit-button" @click="submitPhoneNumber">
      Submit
    </button>
  </div>
  <p>phoneNumber: {{ phoneNumber }}</p>
  <br>
  <p>activeInputIndex: {{ activeInputIndex }}</p>
</template>


<script>
import "bootstrap/dist/css/bootstrap.css";

export default {
  data() {
    return {
      phoneNumber: ["", "", "", "", "", "", "", "", "", ""],
      eventAcceptedKeys: [
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
        "Tab",
        "Enter",
      ],
      activeInputIndex: null,
    };
  },
  mounted() {
    this.$refs.digitInputs[0].focus(); //when component is mounted, focus will be on the first input box
  },
  methods: {
    submitPhoneNumber() {
      alert("Submitted");
    },
    preventInput(index, event, key) {
      event.preventDefault();
      if (key) {
        this.inputKey(index, key);
      } else {
        if (this.eventAcceptedKeys.includes(event.key)) {
          this.inputKey(index, event.key);
        }
      }
    },
    inputKey(index, key) {
      if (key === "ArrowRight" || key === "Tab") {
        if (index < 9) {
          this.$refs.digitInputs[index + 1].focus();
        }
      } else if (key === "ArrowLeft") {
        if (index > 0) {
          this.$refs.digitInputs[index - 1].focus();
        }
      } else if (key === "Enter") {
        this.submitPhoneNumber();
      } else {
        this.phoneNumber[index] = "";
        if (key === "Backspace" || key === "Delete") {
          if (index > 0) {
            this.$refs.digitInputs[index - 1].focus();
          }
        } else {
          this.phoneNumber[index] = key;
          if (index < 9) {
            this.$refs.digitInputs[index + 1].focus();
          }
        }
      }
    },
    addDigit(digit) {
      this.phoneNumber[this.activeInputIndex] = digit // puts that input box as the digit pressed
      if (this.activeInputIndex < 9) {
        this.$refs.digitInputs[this.activeInputIndex + 1].focus() // focus on the next input box
      }
    },
    deleteDigit(digit) {
      this.phoneNumber[this.activeInputIndex] = '' // clear the selected input box
      if (this.activeInputIndex > 0) {
        this.$refs.digitInputs[this.activeInputIndex - 1].focus() // focus on previous input box
      }
    },
    clearDigits() {
      this.phoneNumber.fill(''); // clear phone number
      this.$refs.digitInputs[0].focus() // focus back on the first input box
    }
  },
};
</script>


<style scoped>

@font-face {
  /* THIS IS ILLEGAL TO USE - JUST FOR TEMPORARY VISUAL ONLY */
  font-family: 'my-font';
  src: url('../fonts/Trajan_Bold.ttf') format('truetype');
}

.my-element {
  font-family: 'my-font';
  /* Add other styles as needed */
}

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
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px 0;
  }

  .digit-box {
    border: 1px solid #ced4da;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    width: 5%;
    height: 50px;
    margin: 5px;
  }

  .digit-box input[type="tel"] {
    border: none;
    font-size: 24px;
    text-align: center;
    width: 100%;
  }

  .keypad-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 20px 0;
    padding: 20px;
    width: 350px;
  }

  .key {
    border: 1px solid #ced4da;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    width: 80px;
    height: 80px;
    margin: 5px;
    cursor: pointer;
    background-color: transparent;
    outline: none;
  }

  .key:focus {
    box-shadow: 0 0 0 2px #007bff;
  }

  .submit-button {
    border: none;
    border-radius: 0.25rem;
    background-color: #007bff;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    cursor: pointer;
    margin-top: 20px;
  }

  .submit-button:hover {
    background-color: #0062cc;
  }

  .large-keypad {
  max-width: 600px;
  margin: 0 auto;
}

  @media (max-width: 768px) {
    .digit-box {
      margin-right: 5px;
      width: 35px;
      height: 35px;
      font-size: 20px;
    }

    .digit-box input[type="tel"] {
      width: 35px;
      height: 35px;
      font-size: 20px;
    }

    .submit-button {
      font-size: 16px;
      padding: 8px 16px;
    }
  }
</style>

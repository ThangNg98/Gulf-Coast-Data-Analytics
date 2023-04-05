<template>
    <Transition name="bounce">
      <div class="alert-modal alert alert-secondary alert-dismissible fade show" role="alert" v-if="isVisible">
        <h4 class="alert-heading">{{ title }}</h4>
        <p>{{ message }}</p>
        <div class="btn-group alert-modal-buttons" role="group" aria-label="Modal buttons">
            <button type="button" class="btn btn-success custom-button" @click="closeModalWithYes">Yes</button>
            <button type="button" class="btn btn-danger custom-button" @click="closeModalWithNo">No</button>
        </div>
      </div>
    </Transition>
  </template>
  
  <script>
  export default {
    props: {
      title: {
        type: String,
        default: "Alert"
      },
      message: {
        type: String,
        default: ""
      }
    },
    data() {
      return {
        isVisible: true
      };
    },
    methods: {
      closeModalWithNo() {
        this.isVisible = false;
        this.$emit("close", "no");
      },
      closeModalWithYes() {
        this.isVisible = false;
        this.$emit("close", "yes");
      }
    }
  };
  </script>
  
  <style scoped>
  .alert-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 1rem 1.25rem;
    width: 400px;
    max-width: 90%;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  
  .alert-modal h4 {
    margin-bottom: 0.5rem;
    text-align: left;
  }
  
  .alert-modal p {
    margin-bottom: 0;
    text-align: left;
  }
  
  .alert-modal-close-button {
    border: none;
    background: transparent;
    font-size: 1.5rem;
    cursor: pointer;
  }
  
  .bounce-enter-active {
    transform: translate(-50%, -50%);
    animation: bounce-in 0.5s;
  }
  
  .bounce-leave-active {
    transform: translate(-50%, -50%);
    animation: bounce-in 0.5s reverse;
  }
  
  @keyframes bounce-in {
    0% {
      transform: translate(-50%, -50%) scale(0);
    }
    50% {
      transform: translate(-50%, -50%) scale(1.25);
    }
    100% {
      transform: translate(-50%, -50%) scale(1);
    }
  }

  .custom-button {
    margin-right: 1rem;
    border-radius: 0;
    font-weight: bold;
    transition: background-color 0.3s;
  }
  .custom-button:hover {
    background-color: #5cb85c;
    border-color: #5cb85c;
  }
  .custom-button.btn-danger:hover {
    background-color: #8B0000;
    border-color: #8B0000;
  }

  .alert-modal-buttons {
  display: flex;
  justify-content: flex-start;
}
  </style>
  
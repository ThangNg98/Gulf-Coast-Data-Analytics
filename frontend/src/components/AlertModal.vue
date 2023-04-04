<template>

  <Transition name="bounce">
    <div class="alert-modal alert alert-danger alert-dismissible fade show" role="alert" v-if="isVisible">
      <h4 class="alert-heading">{{ title }}</h4>
      <p>{{ message }}</p>
      <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
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
    }
  },
  methods: {
    closeModal() {
      this.isVisible = false;
      this.$emit("close");
    }
  }
}
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
}

.alert-modal p {
  margin-bottom: 0;
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

</style>
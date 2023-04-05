<template>
  <div class="container">
    <!--Header-->
    <h1 class="text-center my-5">Administrator Login</h1>
    <!--Form for Admin Login-->
    <form ref="login-form" @submit.prevent="handleLogin" novalidate>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">
            <i class="bi bi-person-fill"></i>
          </span>
        </div>
        <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username" ref="validationUsername" pattern="^.*\S+.*$" required :disabled="showModal">
        <div class="invalid-feedback">
          Please enter a username.
        </div>
      </div>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">
            <i class="bi bi-lock-fill"></i>
          </span>
        </div>
        <input type="password" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" v-model="password" ref="validationPassword" pattern="^.*\S+.*$" required :disabled="showModal">
        <div class="invalid-feedback">
          Please enter a password.
        </div>
      </div>      

      <!--Submit Button-->
      <div class="text-center mb-3">
          <button type="submit" class="btn btn-primary">Login</button>
      </div>

    </form>

    <Transition name="bounce">
        <alert-modal v-if="showModal" @close="closeAlertModal" :title="title" :message="message" />
    </Transition>




  </div>
</template>


<script>
//Import "useAdminLoginStore" to save logged in status as session
import { useAdminLoginStore } from '@/stores/AdminLoginStore'
import AlertModal from '@/components/AlertModal.vue';



export default {
  components: {
    AlertModal,
  },
  data() {
    return {
      //variable to hold username
      username: 'admin1',
      //variable to hold password - need to store as hash
      password: 'admin1',
      errorMessage: null,
      showErrorMessage: false,
      showModal: false,
      title: '',
      message: '',
    }
  },
  watch: {
    username(newValue, oldValue) {
      this.removeValidationStyles()
    },
    password(newValue, oldValue) {
      this.removeValidationStyles()
    },
  },
  methods: {
    showAlertModal() {
      this.showModal = true;
      this.title = 'Login Failed';
      this.message = 'Invalid Login Credentials. Please try again.';
    },
    closeAlertModal() {
      this.showModal = false;
      this.title = '';
      this.message = '';
    },
    removeValidationStyles() {
      const form = this.$refs['login-form']
      form.classList.remove('was-validated')
    },
    handleLogin() {
      // Get a reference to the form element
      const form = this.$refs['login-form']

      // Manually trigger the validation and apply the styles
      if (form.checkValidity() === false) {
        form.classList.add('was-validated')
        return
      }

      // Perform your login logic here
      if (this.username == 'admin1' && this.password == 'admin1') {
        //calls the "login()" action from the store file, which sets isLoggedIn state to true
        console.log('isLoggedIn store: ', useAdminLoginStore().isLoggedIn)
        useAdminLoginStore().login()
        console.log('isLoggedIn store: ', useAdminLoginStore().isLoggedIn)
        this.$router.push('/admin/dash')
      }
      else {
        this.showAlertModal()
        // Remove validation state classes from input fields
        const usernameInput = this.$refs['validationUsername']
        const passwordInput = this.$refs['validationPassword']
        usernameInput.classList.remove('is-valid', 'is-invalid')
        passwordInput.classList.remove('is-valid', 'is-invalid')

        form.classList.remove('was-validated')
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

</style>


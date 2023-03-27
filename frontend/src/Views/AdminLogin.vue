<template>
  <div class="container">
    <!--Header-->
    <h1 class="text-center my-5">Administrator Login</h1>
    <!--Form for Admin Login-->
    <form @submit.prevent="handleLogin">
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">
            <i class="bi bi-person-fill"></i>
          </span>
        </div>
        <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username">
      </div>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">
            <i class="bi bi-lock-fill"></i>
          </span>
        </div>
        <input type="password" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" v-model="password">
      </div>
      <br>
      <!--Submit Button-->
      <div class="text-center">
          <button type="submit" class="btn btn-primary">Login</button>
      </div>
    </form>
    <div></div>
    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>

  </div>
</template>

<script>
//Import "useAdminLoginStore" to save logged in status as session
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

export default {
  data() {
    return {
      //variable to hold username
      username: 'admin1',
      //variable to hold password - need to store as hash
      password: 'admin1',
      errorMessage: null
    }
  },
  methods: {
    //method to log admin in
    handleLogin() {
      if (this.username == 'admin1' && this.password == 'admin1') {
        //calls the "login()" action from the store file, which sets isLoggedIn state to true
        console.log('isLoggedIn store: ', useAdminLoginStore().isLoggedIn)
        useAdminLoginStore().login()
        console.log('isLoggedIn store: ', useAdminLoginStore().isLoggedIn)
        this.$router.push('/admindashview')
      }
      else {
        this.errorMessage = 'Login Failed'
      }
    }
  },
  mounted() {
    console.log('mounted isLoggedIn: ', useAdminLoginStore().isLoggedIn)
  }
}
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: auto;
}
</style>
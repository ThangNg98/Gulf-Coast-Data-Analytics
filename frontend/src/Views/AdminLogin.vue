<template>
  <div class="container">
    <!--Header-->
    <h1 class="text-center my-5">Administrator Login</h1>
    <!--Form for Admin Login-->
    <form @submit.prevent="handleLogin">
      <!--User Name input field-->
      <div class="form-group">
        <label for="username">User Name</label>
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
      <!--Password Input Field-->
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" v-model="password">
      </div>
      <br>
      <!--Submit Button-->
      <div class="text-center">
          <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
//Import "useAdminLoginStore" to save logged in status as session
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

export default {
  data() {
    return {
      //variable to hold username
      username: '',
      //variable to hold password - need to store as hash
      password: ''
    }
  },
  computed: {
    // code to check if admin is logged in - used to redirect user later to admin dashboard
    isLoggedIn() {
      useAdminLoginStore().isLoggedIn
    }
  },
  methods: {
    //method to log admin in
    handleLogin() {
      //calls the "login()" action from the store file, which sets isLoggedIn state to true
      useAdminLoginStore().login()
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

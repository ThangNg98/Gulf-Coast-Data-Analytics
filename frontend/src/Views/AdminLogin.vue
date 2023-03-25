<template>
  <div class="container">
    <!--Header-->
    <h1 class="text-center my-5">Administrator Login</h1>
    <!--Form for Admin Login-->
    <form @submit.prevent="handleLogin">
      <!--User Name input field-->
      <div class="form-group">
        <label for="username">User Name</label>
        <object type="image/svg+xml" :data="personIcon" class="icon fa-la"></object>
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
    <p>username: {{ username }}</p>
    <p>password: {{ password }}</p>
    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
//Import "useAdminLoginStore" to save logged in status as session
import { useAdminLoginStore } from '@/stores/AdminLoginStore'

import personIcon from 'bootstrap-icons/icons/person-square.svg';


export default {
  data() {
    return {
      //variable to hold username
      username: 'admin1',
      //variable to hold password - need to store as hash
      password: 'admin1',
      errorMessage: null,
      personIcon: personIcon
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
        this.$router.push('/admindash')
      }
      else {
        this.errorMessage = 'Login Failed'
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

.form-floating {
  position: relative;
}

.icon {
  position: absolute;
  top: calc(50%);
}
</style>
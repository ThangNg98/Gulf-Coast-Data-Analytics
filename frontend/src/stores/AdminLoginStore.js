//import store functionality from pinia
import { defineStore } from 'pinia'

// create a function called "useAdminLoginStore" that holds login status as a session state, and actions to change that session state
export const useAdminLoginStore = defineStore('adminlogin', {
  //session state that determines whether user is logged in
  state: () => ({
    isLoggedIn: false
  }),
  //actions that can be called by Vue components to log the user in and log them out
  actions: {
    login() {
      this.isLoggedIn = true
    },
    logout() {
      this.isLoggedIn = false
    }
  }
})

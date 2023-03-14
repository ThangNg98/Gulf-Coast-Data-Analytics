import { defineStore } from 'pinia'

export const useAdminLoginStore = defineStore('adminlogin', {
  state: () => ({
    isLoggedIn: false
  }),
  actions: {
    login() {
      this.isLoggedIn = true
    },
    logout() {
      this.isLoggedIn = false
    }
  }
})

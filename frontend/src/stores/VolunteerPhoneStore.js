//import store functionality from pinia
import { defineStore } from 'pinia'

// create a function called "useVolunteerPhoneStore" that holds login status as a session state, and actions to change that session state
export const useVolunteerPhoneStore = defineStore('volunteerphone', {
  //session state that determines whether user is logged in
  state: () => ({
    volunteerPhone: null,
    volunteerID: null,
    volunteer_first_name: null
  }),
  //actions that can be called by Vue components to log the user in and log them out
  actions: {
    setVolunteerPhone(phone, ID, name) {
      this.volunteerPhone = phone
      this.volunteerID = ID
      this.volunteer_first_name = name

    },
    clearVolunteerPhone() {
      this.volunteerPhone = null
    }
  },
  persist: {
    enabled: true
  }
})

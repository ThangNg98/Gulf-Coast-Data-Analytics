import { createApp, watch } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap"
import axios from 'axios';
import { createPinia } from 'pinia'
import piniaPersist from 'pinia-plugin-persist'
import "bootstrap-icons/font/bootstrap-icons.css"

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPersist)

app.use(router)
app.use(pinia)

app.mount('#app')

watch(
  pinia.state,
  (state) => {
    localStorage.setItem("stateVolunteerPhone", state.volunteerphone.volunteerPhone);
    localStorage.setItem("stateVolunteerID", state.volunteerphone.volunteerID);
  },
  { deep: true }
  );
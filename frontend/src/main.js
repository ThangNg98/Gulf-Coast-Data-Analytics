import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap"
import axios from 'axios';
import { createPinia } from 'pinia'
import piniaPersist from 'pinia-plugin-persist'
import "bootstrap-icons/font/bootstrap-icons.css"
import 'vue-transition-css/dist/css/vue-transition.css'

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPersist)

app.use(router)
app.use(pinia)

app.mount('#app')


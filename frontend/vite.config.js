import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
   // Phil says: if you want to run the development server on your network so you can access the app on your phone, un-comment this block of code (highlight -> crtl+/), then replace '10.0.0.10' with your computer's IP address.
  // server: {
  //   host: '10.0.0.10'
  // }
})

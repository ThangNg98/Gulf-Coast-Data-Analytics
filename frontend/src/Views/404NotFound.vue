<template>
    <div class="container d-flex flex-column align-items-center justify-content-center">
      <h1 class="mb-4">404 Not Found</h1>
      <button @click="redirectUser" class="btn btn-primary">Home</button>
    </div>
  </template>
  
  <script>
  export default {
    name: '404NotFound',
    data() {
      return {
        redirect: null,
      };
    },
    mounted() {
      const query = new URLSearchParams(this.$route.query);
      if (query.get('volunteer') === 'true') {
        this.redirect = 'volunteer';
      }
      if (query.get('admin') === 'true') {
        this.redirect = 'admin';
      }
    },
    methods: {
      redirectUser() {
        if (this.redirect === 'volunteer') {
          this.$router.push('/');
        } else if (this.redirect === 'admin') {
          this.$router.push('/adminlogin');
        }
      },
    },
  };
  </script>
  
  <style></style>
  
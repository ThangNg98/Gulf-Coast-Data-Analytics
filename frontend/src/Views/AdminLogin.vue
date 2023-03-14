<template>
    <div class="container">
      <h1 class="text-center my-5">Administrator Login</h1>
      <form>
        <div class="form-group">
          <label for="username">User Name</label>
          <input type="text" class="form-control" id="username" v-model="username">
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>
        <br>
        <div class="text-center">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
</template>
  
<script>

export default {
    data() {
        return {
            username: '',
            password: ''
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
  
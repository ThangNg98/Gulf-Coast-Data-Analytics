<template>
    <main>
    <div class="container">
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div style="text-align:center"> 
        <h2> New volunteer?</h2>
        <p> Click <router-link to="/register"> here</router-link> to register</p>
    </div>
    <div style="text-align:center"> 
        <h2> Existing volunteer?</h2>
        <p> Click <router-link to="/login"> here</router-link> to sign-in</p>
    </div>
    </div>
    </main>
</template>

<script>

export default {
    name: 'Home',
    data() {
        return {
            msg : "Welcome to The Living Legacy Center"
        }

    }
}
</script>

<style>
.container {
  margin: auto;

}
</style>
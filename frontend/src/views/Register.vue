<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <h3> Volunteer</h3>
        <form>
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="John">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Smith">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="1234567890">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Email</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
                    </div>
                </div>
            </div>
            <br>
            <h3> Emergency Contact</h3>
            <div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="John">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Smith">
                    </div>
                </div>
                <div class="row">
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Phone Number</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="1234567890">
                    </div>
                    <div class="col"> 
                        <label for="exampleFormControlInput1" class="form-label">Email</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
                    </div>
                </div>
                
            </div>
            <div style="text-align:right; margin-top: 2rem">
                <button @click="handleEventUpdate" type="submit" class="btn btn-primary" >Register</button>
          </div>
        </form>
    </div>
    </main>
</template>

<script>

export default {
    name: 'Register',
    data() {
        return {
            msg : "Volunteer Registration Form"
        }

    }
}
</script>

<style>
.container {
  margin: auto;
  padding-left: auto;
  padding-right: auto

}
</style>
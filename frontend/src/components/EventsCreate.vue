<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Garden">

                <label for="exampleFormControlInput1" class="form-label"> Description</label>
                <textarea class="form-control" id="exampleFormControlInput1" placeholder="Living Legacy's Garden"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" >Submit</button>
          </div>
        </form>
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'EventsCreate',
    data() {
        return {
            msg : "Create New Event",
        };

    },
    methods: {
        submitForm() {
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
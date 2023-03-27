<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <form @submit.prevent="submitForm">
            <div>
                <label for="exampleFormControlInput1" class="form-label">Event Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1">

    
                <label for="exampleFormControlInput1" class="form-label"> Description</label>
                <textarea class="form-control" id="exampleFormControlInput1"></textarea>
            </div>
            <br>
            <div style="text-align:right; margin-top: 2rem;">
                <button type="submit" class="btn btn-success" style="margin-right:0.5rem; text-align:left" > <router-link class="nav-link" to="/admin/events"> Back to Events</router-link></button>
                <button type="submit" class="btn btn-primary" style="margin-right:0.5rem" >Update</button>
                <button type="submit" class="btn btn-danger" >Delete</button>
            </div>
        </form>
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 25%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Total Hours</th>
                        <th scope="col">Number of Volunteers</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>[hours]</td>
                            <td>[# volunteers]</td>
                        </tr>
                    </tbody>
                </table>
        </div>
        
    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'EventsUpdate',
    data() {
        return {
            msg : "Update Event",
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
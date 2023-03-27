<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 50%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Organization Name</th>
                        <th scope="col">Address</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td> <router-link class="nav-link" to="/admin/update_org"> UH Garden </router-link></td>
                            <td> <router-link class="nav-link" to="/admin/update_org"> University of Houston, Houston, Texas 77204  </router-link></td>
                        </tr>
                        <tr>
                            <td>UH Tech</td>
                            <td>University of Houston, Houston, Texas 77204 </td>
                        </tr>

                    </tbody>
                </table>
        </div>
        <div style="text-align:right; margin-top: 2rem;">
            <router-link class="nav-link" to="/admin/create_org"> <button type="submit" class="btn btn-success" style="margin-right:0.5rem" >Add New Organization</button> </router-link>
        </div>

    </div>
    </main>
</template>

<script>
import axios from "axios";

export default {
    name: 'Orgs',
    data() {
        return {
            msg : "List of Organizations",
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

.table td {
    word-wrap: break-word;
    min-width: 160px;
    max-width: 160px;
}
</style>
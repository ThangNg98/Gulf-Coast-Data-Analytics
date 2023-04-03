<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container1"> 
        <div class="table-responsive-md">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
                    <thead>
                        <tr>
                        <th scope="col">Organization Name</th>
                        <th scope="col">Address</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="org in orgs"
                        @click="editOrgs(org.org_id)">
                            <td style="text-align:left">{{ org.org_name }}</td>
                            <td style="text-align:left">{{ org.address_line_1 }}</td>
                        </tr>
                    </tbody>
                </table>
        </div>
        <div style="margin-top: 2rem;margin-left: 30%">
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
            orgs:[]
        };
    
    },
    methods: {
        submitForm() {
        },
        getOrgs() {
            axios.get('https://llc.onrender.com/read_orgs')
            .then(response => {
                // iterate through JSON response and add orgs to orgs array
                for (var i = 0; i < response.data.length; i++) {
                    this.orgs.push(response.data[i]);
                }
            })
            .catch(error => {
                console.log(error);
            });
        },
        editOrgs(org_id) {
            this.$router.push({ name: 'OrgsUpdate', params: 
            { org_id: org_id } });
        }
    },
    mounted() {
        this.getOrgs();
    }
}
</script>

<style scoped>
.container1 {
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
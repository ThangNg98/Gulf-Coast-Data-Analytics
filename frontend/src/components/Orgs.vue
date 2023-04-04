<template>
    <main>
    <div>
        <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
    </div>
    <div class="container1"> 
        <div class="table-responsive-md table-wrapper">
            <table class="table table-bordered" style="margin:auto; text-align: center; max-width: 30%; margin-top: 2rem">
                    <thead class="theadsticky">
                        <tr>
                        <th scope="col">Organization Name</th>
                        <th scope="col">Address</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                        v-for="org in orgs"
                        @click="editOrgs(org.org_id)" :key="org.org_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === org.org_id }"
                        @mouseenter="hoverId = org.org_id"
                        @mouseleave="hoverId = null">
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

    <Transition name="bounce">
        <SuccessModal v-if="successModal" @close="closeSuccessModal" :title="title" :message="message" />
    </Transition>

    </main>
</template>

<script>
import axios from "axios";
import SuccessModal from './SuccessModal.vue'
export default {
    name: 'Orgs',
    components: {
        SuccessModal
    },
    data() {
        return {
            msg : "List of Organizations",
            orgs:[],
            hoverId: null,
            successModal: false,
            title: '',
            message: '',
            isMounted: false
        }
    
    },
    updated() {
        if (!this.isMounted) {
            console.log('pseudo mount')
            const query = new URLSearchParams(this.$route.query);
            if (query.get('success') === 'true') {
                console.log('success is true')
                this.successModal = true;
                this.title = "Success!"
                this.message = "Organization successfully created."
            }
            this.isMounted = true
        }
    },
    methods: {
        closeSuccessModal() {
            this.successModal = false;
            this.title = '';
            this.message = '';
        },
        submitForm() {
        },
        getOrgs() {
            axios.get('http://127.0.0.1:5000/read_orgs')
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
.theadsticky {
  position: sticky;
  top: 0;
  background-color: #e6e7eb !important;
}

.hoverRow {
    background-color: rgba(230, 231, 235, 1);
    transition: background-color 0.3s ease-in-out;
  }
  
.table-wrapper {
  max-height: 700px;
  overflow: auto;
  display:inline-block;
  width: 90%;
}
</style>
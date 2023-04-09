<template>
    <main>
      <div class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-6">
      <div class="row">
        <div class="col-12 text-center mb-3">
          <h1>{{ msg }}</h1>
        </div>
        <div class="col-12 mb-3">
          <div class="text-start">
            <h4>Search Organization By</h4>
          </div>
          <select
            class="form-select"
            v-model="searchBy"
          >
            <option value="Organization Name">Organization Name</option>
            <option value="Organization Address">Organization Address</option>
          </select>
        </div>
        <div v-if="searchBy === 'Organization Name'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="name"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter organization name"
          />
        </div>
        <div v-if="searchBy === 'Organization Address'" class="col-12 mb-3">
          <input
            type="text"
            class="form-control"
            v-model="address"
            v-on:keyup.enter="handleSubmitForm"
            placeholder="Enter organization address"
          />
        </div>
        <div class="col-12 d-flex justify-content-end gap-2">
          <button
            class="btn btn-outline-secondary"
            @click="clearSearch"
            type="submit"
          >
            Clear Search
          </button>
          <button
            class="btn btn-primary"
            @click="handleSubmitForm"
            type="submit"
          >
            Search Organizations
          </button>
        </div>
      </div>
    </div>
  </div>
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
                        <tr v-for="org in orgsFiltered"
                        @click="editOrgs(org.org_id)"
                        :key="org.org_id"
                        :style="{ cursor: 'pointer' }"
                        :class="{ 'hoverRow': hoverId === org.org_id}"
                        @mouseenter="hoverId = org.org_id"
                        @mouseleave="hoverId = null"
                        >
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

    <Transition name="bounce">
        <UpdateModal v-if="updateModal" @close="closeUpdateModal" :title="title" :message="message" />
    </Transition>

    <Transition name="bounce">
        <DeleteModal v-if="deleteModal" @close="closeDeleteModal" :title="title" :message="message" />
    </Transition>

    <div>
        <LoadingModal v-if="isLoading"></LoadingModal>
    </div>

    </main>
</template>

<script>
import axios from "axios";
import SuccessModal from './SuccessModal.vue'
import UpdateModal from './UpdateModal.vue'
import DeleteModal from './DeleteModal.vue'
import LoadingModal from './LoadingModal.vue'
import { useLoadingStore } from '../stores/LoadingStore'
import { getOrgsAPI } from '../api/api.js'

export default {
    name: 'Orgs',
    components: {
        SuccessModal,
        UpdateModal,
        DeleteModal,
        LoadingModal,
    },
    data() {
        return {
            msg : "List of Organizations",
            orgs:[],
            hoverId: null,
            successModal: false,
            updateModal: false,
            deleteModal: false,
            title: '',
            message: '',
            isMounted: false,
            searchBy: '',
            name: '',
            address: '',
            orgsFiltered: [],
            isLoading: false,
        };
    
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
            if (query.get('update') === 'true') {
                console.log('update is true')
                this.updateModal = true;
                this.title = "Updated!"
                this.message = "Organization successfully updated."
            }
            if (query.get('delete') === 'true') {
                console.log('delete is true')
                this.deleteModal = true;
                this.title = "Deleted!"
                this.message = "Organization successfully deleted."
            }
            this.isMounted = true
        }
    },
    mounted() {
        this.loadData();
    },
    methods: {
      async loadData() {
        this.isLoading = true;
        try {
          const response = await getOrgsAPI();
          // iterate through JSON response and add orgs to orgs array
          for (var i = 0; i < response.data.length; i++) {
              this.orgs.push(response.data[i]);
          }
          this.setOrgsList()
        } catch (error) {
          console.log(error)
        };
        this.isLoading = false;
      },
        closeSuccessModal() {
            this.successModal = false;
            this.title = '';
            this.message = '';
        },
        closeUpdateModal() {
            this.updateModal = false;
            this.title = '';
            this.message = '';
        },
        closeDeleteModal() {
            this.deleteModal = false;
            this.title = '';
            this.message = '';
        },
        setOrgsList() {
            this.orgsFiltered = this.orgs
        },
        editOrgs(org_id) {
            this.$router.push({ name: 'OrgsUpdate', params: 
            { org_id: org_id } });
        },
        handleSubmitForm() {
        //if user searched by Organization name
            if (this.searchBy === 'Organization Name') {
            //filter the Organizations list by Organization name
                this.orgsFiltered = this.orgs.filter((org) => org.org_name.toLowerCase().includes(this.name.toLowerCase()));
            } 
            //if user searched by Organization address
            else if (this.searchBy === 'Organization Address') {
                //filter the Organizations list by Organization address
                this.orgsFiltered = this.orgs.filter((org) => org.address_line_1.toLowerCase().includes(this.address.toLowerCase()));
            }
        },
        //method called when user clicks "Clear Search" button
        clearSearch() {
            // Resets all the variables
            this.searchBy = ''
            this.name = ''
            this.address = ''
            this.setOrgsList()
        },
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
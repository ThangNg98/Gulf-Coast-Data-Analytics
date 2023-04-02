<template>
  <main class="flex flex-row">
    <div id="_container" class="h-auto">
      <header class="w-full">
        <section style="margin-left: 2rem; margin-top: 2rem">
          <nav class="navbar navbar-expand-lg navbar-dark navbar-brand" style="background-color: #060f3f; margin-bottom:1rem">
            <img class="img-fluid" style="max-width: 100%; margin-bottom: 0px" src="@\assets\llc_logo.png" />
            <button
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              class="navbar-toggler"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation" style="margin-top:1rem;">
              
              <span class="navbar-toggler-icon"></span> Menu
            </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 flex-wrap">
                  <li class="nav-item">
                    <router-link class="nav-link" to="/"> Home </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link class="nav-link" to="/register"> Register </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link class="nav-link" to="/profile/checkin"> Volunteer Profile </router-link>
                  </li>
                  
                </ul>
            </div>
      </nav>
        </section>
      </header>

    </div>
    
    <div class="grow w-4/5">
      <div>
        <router-view></router-view>
      </div>
    </div>
    <div class="footer">
      <div class="footer-content">

      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      org: '',
    }
  },

  name: "App",
};
</script>

<style>
#_container {
  background-color: #060f3f;
  color: white;
  padding: 18px;
}
 

</style>

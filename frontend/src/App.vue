<template>
  <main class="flex flex-row">
    <div id="_container" class="h-auto">
      <header class="w-full">
        <section class="float-left" style="margin-left: 5rem; margin-top: 2rem">
          <img class="" style="width: 300px; margin-bottom: 0px" src="@\assets\llc_logo.png" />
          <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #060f3f;">
          <div class="container-fluid " >
            <div class="collapse navbar-collapse" id="navbarSupportedContent " >
              <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <router-link class="nav-link" to="/"> Home </router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" to="/register"> Register </router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" to="/register"> Volunteer Sign-in </router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link" to="/register"> Admin </router-link>
                </li>
                
              </ul>
            </div>
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

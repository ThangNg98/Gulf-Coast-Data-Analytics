<template>
  <main class="flex flex-row">
    <!--header-->
    <div id="_container" class="h-auto text-start">
      <header class="w-full">
        <section style=" margin-top: .5rem">
            <img class="img-fluid" style="width: 10rem; max-width: 100%; margin-bottom: .5rem" src="@\assets\llc_logo.png" />
        </section>
      </header>
    </div>
    
    <!--body-->
    <div class="grow w-4/5" style="padding-bottom: 10rem;">
      <div>
        <router-view></router-view>
      </div>
    </div>
    
    <!--footer-->
    <div id="_container" class="h-auto w-100 position-absolute bottom-0 text-start">
      <footer class="w-full">
        <section style="margin-top: .5rem">
          <div class="ms-0 " style="color:grey;">The Living Legacy Center is a 501(c)(3) tax-exempt charity. <br>Copyright © 2021 All Rights Reserved</div>
        </section>


      </footer>
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

<template>  
<div class="h-100 d-flex flex-column p-3 text-white bg-dark" style="min-width: 150px;">
  <div>
    <img src="@/assets/logo.png" height="40" width="40">
    <span class="p-3">{{ today }}</span>
  </div>
    <hr>
    <div class="nav nav-pills flex-column">
      <router-link class="nav-link text-white" to="/">Dashboard</router-link>
    </div>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      <span class="p-1">Seoul Eats</span>
      <router-link class="nav-link text-white" to="/seoulEats/todo">To-do</router-link>
      <router-link class="nav-link text-white" to="/seoulEats/inventory">Inventory Check</router-link>
      <router-link class="nav-link text-white" to="/seoulEats/history">Item Tracker</router-link>
      <hr>
      <a>Tokyo Eats</a>
      <router-link class="nav-link text-white" to="/tokyoEats/todo">To-do</router-link>
      <router-link class="nav-link text-white" to="/tokyoEats/inventory">Inventory Check</router-link>
      <router-link class="nav-link text-white" to="/tokyoEats/history">Item Tracker</router-link>
      <hr>      
    </ul>


    <div class="dropdown">
      <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
        <strong class="p-1">Username</strong>
      </a>
      <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
        <li v-if="isAdmin"><a class="dropdown-item" href="/admin">Admin</a></li>
        <li><a class="dropdown-item" href="#">Settings</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">Logout</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAdmin: false,
      today: ''
    }
  },
  mounted() {
    this.isAdmin = window.sessionStorage.getItem("isAdmin")
    const date = new Date();
      let currentDay = String(date.getDate()).padStart(2, '0');
      let currentMonth = String(date.getMonth() + 1).padStart(2, "0");
      let currentYear = date.getFullYear();
      this.today = `${currentDay}-${currentMonth}-${currentYear}`;
  },
}
</script>

<style>
a.router-link-active {
  background-color: #A567EB;
}
</style>
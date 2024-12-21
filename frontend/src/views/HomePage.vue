<template>
    <div>
      <h1><router-link :to="{ name : 'Home'}">Home</router-link></h1>
      <h1 v-if="username">Welcome, {{ username }}!</h1>
      <h1 v-else>Welcome to Clicker</h1>
      <p v-if="!username">
        Please <router-link :to="{ name : 'Login'}">Login</router-link> or <router-link :to="{ name : 'Register'}">Register</router-link>
      </p>
      <div v-if="username">
        <router-link :to="{ name : 'Click'}">Go to Clicker</router-link>
        <router-link :to="{ name : 'Profile'}">Profile</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: localStorage.getItem('username') || '',
      };
    },
  };
  </script>
  
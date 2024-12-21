<template>
    <div>
      <h1><router-link :to="{ name : 'Home'}">Home</router-link></h1>
      <h1>Profile</h1>
      <p>Username: {{ username }}</p>
      <button @click="logout">Logout</button>
      <button @click="deleteAccount">Delete Account</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        username: localStorage.getItem('username') || '',
      };
    },
    methods: {
      logout() {
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        localStorage.removeItem('username');
        this.$router.push('/auth/login');
      },
      async deleteAccount() {
        try {
          await axios.delete('auth/delete-account/');
          this.logout();
        } catch (err) {
          console.error(err);
        }
      },
    },
  };
  </script>
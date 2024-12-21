<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username</label>
          <input v-model="username" id="username" type="text" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input v-model="password" id="password" type="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="error" style="color:red">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/auth/login/', {
            username: this.username,
            password: this.password,
          });
          localStorage.setItem('access', response.data.access);
          localStorage.setItem('refresh', response.data.refresh);
          localStorage.setItem('username', this.username); // Store username
          this.$router.push('/');
        } catch (err) {
          this.error = 'Invalid credentials';
        }
      },
    },
  };
  </script>
<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Username</label>
          <input v-model="username" id="username" type="text" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input v-model="email" id="email" type="email" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input v-model="password" id="password" type="password" required />
        </div>
        <div>
          <label for="password2">Confirm Password</label>
          <input v-model="password2" id="password2" type="password" required />
        </div>
        <button type="submit">Register</button>
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
        email: '',
        password: '',
        password2: '',
        error: '',
      };
    },
    methods: {
      async register() {
        try {
          await axios.post('auth/register/', {
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.password2,
          });
          this.$router.push('/auth/login');
        } catch (err) {
          this.error = 'Registration failed';
        }
      },
    },
  };
  </script>
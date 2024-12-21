<template>
    <div>
      <h1><router-link :to="{ name : 'Home'}">Home</router-link></h1>
      <h1>Clicker Game</h1>
      <p>Clicks: {{ clicks }}</p>
      <button @click="increment">Click Me!</button>
      <h2>Leaderboard</h2>
      <ul>
        <li v-for="user in leaderboard" :key="user.user">
          {{ user.username }}: {{ user.clicks }} clicks
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        clicks: 0,
        leaderboard: [],
        username: localStorage.getItem('username') || '',
      };
    },
    methods: {
      async increment() {
        this.clicks++;
        try {
          await axios.post('click/', { clicks: this.clicks });
          this.getLeaderboard();
        } catch (err) {
          console.error(err);
        }
      },
      async getLeaderboard() {
        try {
          const response = await axios.get('leaderboard/');
          this.leaderboard = response.data;
        } catch (err) {
          console.error(err);
          console.log('에러발생 비상비상')
        }
      },
    },
    mounted() {
      this.getLeaderboard();
    },
  };
  </script>
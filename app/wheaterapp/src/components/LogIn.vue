<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="username" id="username" />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" id="password" />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>

  import { useToast } from 'vue-toast-notification';
  import {Axios} from 'axios';

  const $axios = new Axios({
    baseURL: 'http://13.60.163.212/:8002'
  });




  const $toast = useToast();

  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      async login() {
  try {
    const res = await $axios.get('http://13.60.163.212:8002/users', {
      params: {
        username: this.username,
        password: this.password
      }
    });
    if (res.data.length > 2) {
      localStorage.setItem('authenticated', 'true');
      this.$router.push('/dashboard');
    } else {
      $toast.error('Invalid credentials');
    }
  } catch (error) {
    console.error('Error during login:', error);
    $toast.error('An error occurred during login.');
  }
}

    }
  };
  </script>
  
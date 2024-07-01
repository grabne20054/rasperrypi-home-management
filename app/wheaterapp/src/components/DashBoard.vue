<template>
  <div>
    <h2>Dashboard WheaterData</h2>

    
    <div v-if="weatherData">
      <p>Location: {{ weatherData }}</p>
      <p>Temperature: {{ weatherData.temperature }}°C</p>
      <p>Humidity: {{ weatherData.humidity }}%</p>
    </div>
    
    <div v-else>
      <p>Loading weather data...</p>
    </div>
    
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

const $toast = useToast();

export default {
  data() {
    return {
      weatherData: null
    };
  },
  methods: {
    async fetchWeatherData() {
      try {
        const response = await axios.get('http://localhost:8002/wheaterdata');
        this.weatherData = response.data;
      } catch (error) {
        console.error('Error fetching weather data:', error);
        $toast.error('An error occurred while fetching weather data.');

      }
    },
    async fetchLocation(id) {
      try {
        const response = await axios.get('http://localhost:8002/location/' + id);
        this.weatherData = response.data;
      } catch (error) {
        console.error('Error fetching location:', error);
        $toast.error('An error occurred while fetching location.');
      }
    },
    logout() {
      localStorage.removeItem('authenticated');
      this.$router.push('/login');
    }
  },
  mounted() {
    this.fetchWeatherData();
  }
};
</script>

<style scoped>
/* Add component-specific styles here */
</style>

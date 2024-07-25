<template>
  <div>
    <WheaterCard/>
    <StatisticCard/>
  </div>
</template>

<script>
import axios from 'axios';
import  WheaterCard  from './WheaterCard.vue';
import  StatisticCard  from './StatisticCard.vue';
import { useToast } from 'vue-toast-notification';

const $toast = useToast();

export default {
  components: {
    WheaterCard,
    StatisticCard
  },
  data() {
    return {
      weatherData: null
    };
  },
  methods: {
    async fetchWeatherData() {
      try {
        const response = await axios.get('http://13.60.163.212:8002/wheaterdata');
        this.weatherData = response.data;
      } catch (error) {
        console.error('Error fetching weather data:', error);
        $toast.error('An error occurred while fetching weather data.');

      }
    },
    async fetchLocation(id) {
      try {
        const response = await axios.get('http://13.60.163.212:8002/location/' + id);
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

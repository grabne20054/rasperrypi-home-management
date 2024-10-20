<template>
  <div class="card-container">
    <div class="top-cards">
      <WheaterCard class="card" />
      <StatisticCard class="card" />
    </div>
    <div class="livestreams">
      
    <LiveStreamCard class="live-stream-card"/>
    
  </div>
  </div>
</template>


<script>
import axios from 'axios';
import WheaterCard from './WheaterCard.vue';
import StatisticCard from './StatisticCard.vue';
import LiveStreamCard from './LiveStreamCard.vue';
import { useToast } from 'vue-toast-notification';


const url = 'http://13.61.15.86:8002';

const $toast = useToast();

export default {
  components: {
    WheaterCard,
    StatisticCard,
    LiveStreamCard
  },
  data() {
    return {
      weatherData: null
    };
  },
  methods: {
    async fetchWeatherData() {
      try {
        const response = await axios.get(url + '/wheaterdata');
        this.weatherData = response.data;
      } catch (error) {
        console.error('Error fetching weather data:', error);
        $toast.error('An error occurred while fetching weather data.');
      }
    },
    async fetchLocation(id) {
      try {
        const response = await axios.get(url + '/location/' + id);
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
.card-container {
  display: flex;
  flex-direction: column; /* Stack cards vertically */
  gap: 20px; /* Add space between the rows of cards */
  padding: 20px; /* Add padding around the container */
  border-radius: 10px; /* Rounded corners for the container */
  background-color: #f5f5f5; /* Light background for the container */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

.top-cards {
  display: flex;
  justify-content: space-between; /* Distribute space between the top cards */
  gap: 20px; /* Add space between top cards */
}

.card {
  flex: 1; /* Take up equal space */
  padding: 20px; /* Inner padding for cards */
  border-radius: 10px; /* Rounded corners for cards */
  background-color: #ffffff; /* White background for cards */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Card shadow */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Animation for hover effect */
}


.card:hover {
  transform: translateY(-5px); /* Lift effect on hover */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
}

/* Optional: Add some additional styling for headings and text inside the cards */
h2 {
  font-size: 1.5rem; /* Larger font size for headings */
  margin-bottom: 10px; /* Space below headings */
}

p {
  font-size: 1rem; /* Standard font size for paragraphs */
  line-height: 1.5; /* Better line spacing */
  color: #555; /* Darker text for readability */
}

/* Responsive Design */
@media (max-width: 768px) {
  .top-cards {
    flex-direction: column; /* Stack top cards on smaller screens */
  }

  .card {
    margin: 0 0 20px 0; /* Margin below each card */
  }

  .live-stream-card {
    height: auto; /* Allow LiveStreamCard to adjust height on smaller screens */
    width: auto;
    display: flex;
  }

}
</style>

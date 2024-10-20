<template>
  <div>
    <select v-model="selectedDataset" @change="updateChartData">
      <option value="temperature">Temperatur</option>
      <option value="humidity">Luftfeuchtigkeit</option>
      <option value="rain_amount">Regenmenge</option>
      <option value="wind_speed">Windgeschwindigkeit</option>
    </select>
    <select v-model="duration" @change="fetchWeatherData">
        <option value="alltime">komplette Zeit</option>
        <option value="lastday">letzter Tag</option>
        <option value="lastsevendays">letzte 7 Tage</option>
      </select>
    <div class="chart-container">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Line } from 'vue-chartjs';
import { getWeatherDataLastSevenDays, getWeatherDataLastDay , getWeatherData,options } from './chartConfig.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default {
  name: 'App',
  components: {
    Line
  },
  data() {
    return {
      selectedDataset: 'temperature',
      weatherData: [],
      duration : 'alltime',
      chartData: {
        labels: [],
        datasets: [{
          label: 'Temperature',
          backgroundColor: 'rgba(255, 99, 132, 0.2)', // Area color
          borderColor: 'rgba(255, 99, 132, 1)', // Line color
          data: []
        }]
      },
      chartOptions: options
    };
  },
  mounted() {
    this.fetchWeatherData();
  },
  methods: {
    async fetchWeatherData() {
      let response;
      try {
        if (this.duration == 'lastsevendays') {
          response = await getWeatherDataLastSevenDays();
          for (let i = 0; i < response.data.length; i++) {
            response.data[i].timestamp = response.data[i].timestamp.split('T')[0];
          }
        } else if (this.duration == 'lastday') {
          response = await getWeatherDataLastDay();
          for (let i = 0; i < response.data.length; i++) {
            response.data[i].timestamp = response.data[i].timestamp.split('T')[1].split('.')[0];
          }
        }
        else if (this.duration == 'alltime') {
          response = await getWeatherData();
          for (let i = 0; i < response.data.length; i++) {
            response.data[i].timestamp = response.data[i].timestamp.split('T')[0];
          }
        }
        this.weatherData = response.data;
        this.updateChartData();
      } catch (error) {
        console.error("Error fetching weather data:", error);
      }
    },
    updateChartData() {
      const labels = this.weatherData.map(item => item.timestamp);
      const dataKey = this.selectedDataset;
      const data = this.weatherData.map(item => item[dataKey]);

      const backgroundColor = this.getBackgroundColor(dataKey);
      const borderColor = this.getBorderColor(dataKey);

      this.chartData = {
        labels: labels,
        datasets: [{
          label: this.capitalize(dataKey),
          backgroundColor: backgroundColor,
          borderColor: borderColor,
          data: data
        }]
      };
    },
    getBackgroundColor(dataset) {
      switch (dataset) {
        case 'temperature':
          return 'rgba(255, 99, 132, 0.2)';
        case 'humidity':
          return 'rgba(54, 162, 235, 0.2)';
        case 'rain_amount':
          return 'rgba(75, 192, 192, 0.2)';
        case 'wind_speed':
          return 'rgba(153, 102, 255, 0.2)';
        default:
          return 'rgba(255, 159, 64, 0.2)';
      }
    },
    getBorderColor(dataset) {
      switch (dataset) {
        case 'temperature':
          return 'rgba(255, 99, 132, 1)';
        case 'humidity':
          return 'rgba(54, 162, 235, 1)';
        case 'rain_amount':
          return 'rgba(75, 192, 192, 1)';
        case 'wind_speed':
          return 'rgba(153, 102, 255, 1)';
        default:
          return 'rgba(255, 159, 64, 1)';
      }
    },
    capitalize(word) {
      return word.charAt(0).toUpperCase() + word.slice(1).replace('_', ' ');
    }
  }
};
</script>

<style>
.chart-container {
  width: 100%; /* Make the container take the full width of its parent */
  height: 600px; /* Set a fixed height for the container */
}

select {
  padding: 10px; /* Add some padding */
  margin: 10px 0; /* Add margin for spacing */
  border: 1px solid #ccc; /* Add border */
  border-radius: 5px; /* Rounded corners */
  font-size: 16px; /* Font size */
  cursor: pointer; /* Change cursor on hover */
  transition: border-color 0.3s ease; /* Smooth transition for border color */
}

select:hover {
  border-color: #007bff; /* Change border color on hover */
}

select:focus {
  outline: none; /* Remove default outline */
  border-color: #007bff; /* Change border color when focused */
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* Add a shadow effect */
}

/* Optional: Style for options */
option {
  padding: 10px; /* Padding for options */
}

@media (max-width: 768px) {
  .chart-container {
    height: 400px; /* Adjust height for smaller screens */
  }
}
</style>


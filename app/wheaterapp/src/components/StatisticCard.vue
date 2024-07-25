<template>
    <div>
      <Line :data="chartData" :options="chartOptions" />
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
  import { getWeatherDataLastSevenDays, options } from './chartConfig.js';
  
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
        chartData: {
          labels: [],
          datasets: [{
          }]
        },
        chartOptions: options
      };
    },
    mounted() {
      this.fetchChartData();
    },
    methods: {
      async fetchChartData() {
        try {
          const response = await getWeatherDataLastSevenDays();
          const dates = [];
          const temperatures = [];
          const humidities = [];
          const rain_amount = [];
          const wind_speed = [];
  
          response.data.forEach(i => {
            dates.push(i.timestamp);
            temperatures.push(i.temperature);
            humidities.push(i.humidity);
            rain_amount.push(i.rain_amount);
            wind_speed.push(i.wind_speed);

          });
          this.chartData = {
            labels: dates,
            datasets: [{
              label: 'Temperatur',
              backgroundColor: 'blue',
              borderColor: 'blue',
              data: temperatures
            },
            {
              label: 'Luftfeuchtigkeit',
              backgroundColor: 'green',
              borderColor: 'green',
              data: humidities
            },
            {
              label: 'Regenmenge',
              backgroundColor: 'red',
              borderColor: 'red',
              data: rain_amount
            },
            {
              label: 'Windgeschwindigkeit',
              backgroundColor: 'yellow',
              borderColor: 'yellow',
              data: wind_speed
            }]
          };
        } catch (error) {
          console.error("Error fetching weather data:", error);
        }
      }
    }
  };
  </script>
  
  <style>
  /* Optional styling */
  </style>
  
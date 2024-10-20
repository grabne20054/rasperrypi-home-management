<template>
    <div class="weather-card">
        <h2>Aktuellstes Wetter: {{ location }}</h2>
        <h3> {{ formattedtime  }}</h3>
        <div class="weather-info temperature">
            <img src="@/assets/thermometer.png" alt="Temperature">
            <span>{{ temperature }}°C</span>
        </div>
        <div class="weather-info">
            <img src="@/assets/humidity.png" alt="Humidity">
            <span>{{ humidity }}%</span>
        </div>
        <div class="weather-info">
            <img src="@/assets/rainy.png" alt="Rain amount">
            <span>{{ rain_amount }} mm</span>
        </div>
        <div class="weather-info ">
            <img src="@/assets/windy.png" alt="Wind speed">
            <span>{{ wind_speed }} km/h</span>
        </div>
    </div>
</template>

<script>
import { getLastWheaterData, getLocation }from  './wheaterConfigs.js';
export default {
    data() {
        return {
            temperature: null,
            humidity: null,
            rain_amount: null,
            wind_speed: null,
            location: null,
            timestamp: null,
            formattedtime: null
        };
    },
    async mounted() {
        this.temperature = (await getLastWheaterData()).data.temperature;
        this.humidity = (await getLastWheaterData()).data.humidity;
        this.rain_amount = (await getLastWheaterData()).data.rain_amount;
        this.wind_speed = (await getLastWheaterData()).data.wind_speed;
        this.location = (await getLocation((await getLastWheaterData()).data.location_id)).data.name;
        this.timestamp = (await getLastWheaterData()).data.timestamp;
        this.formattedtime = this.formatTimestamp(this.timestamp);
    },

    methods: {
        formatTimestamp(timestamp) {
            // Split the timestamp at 'T'
            const [datePart, timePart] = timestamp.split('T');
            
            // Get the date in dd.MM.yyyy format
            const [year, month, day] = datePart.split('-');
            const formattedDate = `${day}.${month}.${year}`;
            
            // Get the time in HH:mm format
            const [hour, minute] = timePart.split(':');
            const formattedTime = `${hour}:${minute}`;
            
            return `${formattedDate} ${formattedTime}`; // Combine date and time
        }

    }
};
</script>

<style scoped>
.weather-card {
    background-color: #bbdefb; /* Lighter blue background */
    border: 1px solid #90caf9; /* Border matching the new color scheme */
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    padding: 20px;
    max-width: 400px; /* Larger card width */
    margin: auto;
}

.weather-card h2 {
    color: #0d47a1; /* Darker blue for the heading */
    margin-bottom: 20px;
    text-align: center;
}

.weather-card h3 
{
    color: #0d47a1; /* Darker blue for the heading */
    margin-bottom: 20px;
    text-align: center;
}

.weather-info {
    margin-bottom: 15px;
    font-size: 25px; /* Slightly larger font size */
    align-content: center;
}

.temperature {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 40px; /* Larger font size for temperature */
    color: #fff;
    margin-bottom: 25px; /* More space below temperature info */
}

.humidity {
    display: flex;
    justify-content: left;
    align-items: left;
    font-size: 35px; /* Larger font size for temperature */
    color: #fff;
    margin-bottom: 25px; /* More space below temperature info */
}

.wind-speed{
    display: flex;
    justify-content: right;
    align-items: right;
    font-size: 35px; /* Larger font size for temperature */
    color: #fff;
    margin-bottom: 25px; /* More space below temperature info */
}


.weather-info img {
    width: 40px;  /* Smaller size */
    height: 40px; /* Smaller size */
    margin-right: 10px;
}

.weather-info span {
    color: #000000; /* Matching blue for the text */
}

@media (max-width: 768px) {
    .weather-card {
        max-width: 100%; /* Full width on smaller screens */
    }
}
</style>

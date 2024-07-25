<template>
    <div class="weather-card">
        <h2>Aktuelles Wetter</h2>
        <h3>Aktualisierungsintervall: 1h</h3>
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
        <div class="weather-info">
            <img src="@/assets/windy.png" alt="Wind speed">
            <span>{{ wind_speed }} km/h</span>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            temperature: null,
            humidity: null,
            rain_amount: null,
            wind_speed: null,
        };
    },
    mounted() {
        this.temperature = 25;
        this.humidity = 70;
        this.rain_amount = 5;
        this.wind_speed = 10;
    },
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
    text-align: left;
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
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    font-size: 25px; /* Slightly larger font size */
}

.temperature {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 40px; /* Larger font size for temperature */
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
</style>

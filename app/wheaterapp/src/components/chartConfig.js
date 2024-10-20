import axios from "axios";

export function getWeatherDataLastSevenDays() {
    return axios.get("http://13.61.15.86:8002/wheaterdata/last-seven-days");
      
}

export function getWeatherDataLastDay() {
    return axios.get("http://13.61.15.86:8002/wheaterdata/last-day");

}

export function getWeatherData() {
    return axios.get("http://13.61.15.86:8002/wheaterdata");
}

export const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

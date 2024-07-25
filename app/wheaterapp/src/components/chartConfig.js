import axios from "axios";

export function getWeatherDataLastSevenDays() {
    return axios.get("http://127.0.0.1:8002/wheaterdata/last-seven-days");
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

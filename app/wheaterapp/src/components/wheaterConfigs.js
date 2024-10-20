import axios from "axios";

export function getLastWheaterData() {
    return axios.get("http://13.61.15.86:8002/wheaterdata/last-entry");

}

export function getLocation(id)
{
    return axios.get(`http://13.61.15.86:8002/locations/${id}`);
}
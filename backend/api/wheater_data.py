from fastapi import APIRouter

from api.model import WheaterDataSchema, WheaterDataDB
from crud import crud


router = APIRouter()

@router.post("/wheaterdata/", response_model=WheaterDataDB, status_code=201)
async def create_wheater_data(wheater_data: WheaterDataSchema):
    wheater_data = await crud.create_wheater_data(wheater_data)
    response_object = {
        "id": wheater_data.id,
        "temperature": wheater_data.temperature,
        "humidity": wheater_data.humidity,
        "wind_speed": wheater_data.wind_speed,
        "rain_amount": wheater_data.rain_amount,
        "timestamp": wheater_data.timestamp,
        "location_id": wheater_data.location_id
    }
    return response_object

@router.get("/wheaterdata/", status_code=200)
async def read_wheater_data():
    wheater_data = await crud.read_wheater_data()
    return wheater_data

@router.get("/wheaterdata/{wheater_data_id}", response_model=WheaterDataDB, status_code=200)
async def read_wheater_data(wheater_data_id: int):
    wheater_data = await crud.read_wheater_data_id(wheater_data_id)
    response_object = {
        "id": wheater_data.id,
        "temperature": wheater_data.temperature,
        "humidity": wheater_data.humidity,
        "wind_speed": wheater_data.wind_speed,
        "rain_amount": wheater_data.rain_amount,
        "timestamp": wheater_data.timestamp,
        "location_id": wheater_data.location_id
    }
    return response_object

@router.put("/wheaterdata/{wheater_data_id}", response_model=WheaterDataDB, status_code=200)
async def update_wheater_data(wheater_data_id: int, wheater_data: WheaterDataSchema):
    wheater_data = await crud.update_wheater_data(wheater_data_id, wheater_data)
    response_object = {
        "id": wheater_data.id,
        "temperature": wheater_data.temperature,
        "humidity": wheater_data.humidity,
        "wind_speed": wheater_data.wind_speed,
        "rain_amount": wheater_data.rain_amount,
        "timestamp": wheater_data.timestamp,
        "location_id": wheater_data.location_id
    }
    return response_object

@router.delete("/wheaterdata/{wheater_data_id}", status_code=204)
async def delete_wheater_data(wheater_data_id: int):
    wheater_data = await crud.delete_wheater_data(wheater_data_id)
    response_object = {
        "id": wheater_data_id           
    }

    return response_object

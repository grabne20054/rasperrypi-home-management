from fastapi import APIRouter

from api.model import LocationSchema, LocationDB
from crud import crud


router = APIRouter()

@router.post("/locations/", response_model=LocationDB, status_code=201)
async def create_location(location: LocationSchema):
    location = await crud.create_location(location)
    response_object = {
        "id": location.id,
        "name": location.name,
        "latitude": location.latitude,
        "longitude": location.longitude
    }
    return response_object

@router.get("/locations/", status_code=200)
async def read_locations():
    locations = await crud.read_locations()
    return locations

@router.get("/locations/{location_id}", response_model=LocationDB, status_code=200)
async def read_location(location_id: int):
    location = await crud.read_location(location_id)
    response_object = {
        "id": location.id,
        "name": location.name,
        "latitude": location.latitude,
        "longitude": location.longitude
    }
    return response_object

@router.put("/locations/{location_id}", response_model=LocationDB, status_code=200)
async def update_location(location_id: int, location: LocationSchema):
    location = await crud.update_location(location_id, location)
    response_object = {
        "id": location.id,
        "name": location.name,
        "latitude": location.latitude,
        "longitude": location.longitude
    }
    return response_object

@router.delete("/locations/{location_id}", status_code=204)
async def delete_location(location_id: int):
    location = await crud.delete_location(location_id)
    response_object = {
        "id": location_id            
    }

    return response_object
    

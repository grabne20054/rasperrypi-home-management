from datetime import datetime
from pydantic import BaseModel

class WheaterDataSchema(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    rain_amount: float
    timestamp: datetime
    location_id: int

class LocationSchema(BaseModel):
    name: str
    latitude: float
    longitude: float

class WheaterDataDB(WheaterDataSchema):
    id: int

class LocationDB(LocationSchema):
    id: int

class UserSchema(BaseModel):
    name: str
    password: str

class UserDB(UserSchema):
    id: int

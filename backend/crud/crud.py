from api.model import WheaterDataSchema, LocationSchema, UserSchema
from db.session import session
from fastapi import HTTPException
from db.model import WheaterData, Location, User

# WheaterData

async def create_wheater_data(wheater_data: WheaterDataSchema):
    new_wheater_data = WheaterData(
        temperature=wheater_data.temperature,
        humidity=wheater_data.humidity,
        wind_speed=wheater_data.wind_speed,
        rain_amount=wheater_data.rain_amount,
        location_id=wheater_data.location_id
    )
    if session.query(Location).filter(Location.id == new_wheater_data.location_id).first() is None:
        raise HTTPException(status_code=404, detail="Location not found")
    session.add(new_wheater_data)
    session.commit()
    session.refresh(new_wheater_data)
    return new_wheater_data

async def read_wheater_data():
    wheater_data = session.query(WheaterData).all()
    return wheater_data

async def read_wheater_data_id(wheater_data_id: int):
    wheater_data = session.query(WheaterData).filter(WheaterData.id == wheater_data_id).first()
    if wheater_data is None:
        raise HTTPException(status_code=404, detail="WheaterData not found")
    return wheater_data

async def update_wheater_data(wheater_data_id: int, wheater_data: WheaterDataSchema):
    wheater_data_db = session.query(WheaterData).filter(WheaterData.id == wheater_data_id).first()
    if wheater_data_db is None:
        raise HTTPException(status_code=404, detail="WheaterData not found")
    wheater_data_db.temperature = wheater_data.temperature
    wheater_data_db.humidity = wheater_data.humidity
    wheater_data_db.wind_speed = wheater_data.wind_speed
    wheater_data_db.rain_amount = wheater_data.rain_amount
    wheater_data_db.location_id = wheater_data.location_id
    session.commit()
    session.refresh(wheater_data_db)
    return wheater_data_db

async def delete_wheater_data(wheater_data_id: int):
    wheater_data_db = session.query(WheaterData).filter(WheaterData.id == wheater_data_id).first()
    if wheater_data_db is None:
        raise HTTPException(status_code=404, detail="WheaterData not found")
    session.delete(wheater_data_db)
    session.commit()
    return None

# Location

async def create_location(location: LocationSchema):
    if session.query(Location).filter(Location.name == location.name).first() is not None:
        raise HTTPException(status_code=400, detail="Location already exists")
    new_location = Location(
        name=location.name,
        latitude=location.latitude,
        longitude=location.longitude
    )
    session.add(new_location)
    session.commit()
    session.refresh(new_location)
    return new_location

async def read_locations():
    locations = session.query(Location).all()
    return locations

async def read_location(location_id: int):
    location = session.query(Location).filter(Location.id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


async def update_location(location_id: int, location: LocationSchema):
    location_db = session.query(Location).filter(Location.id == location_id).first()
    if location_db is None:
        raise HTTPException(status_code=404, detail="Location not found")
    location_db.name = location.name
    location_db.latitude = location.latitude
    location_db.longitude = location.longitude
    session.commit()
    session.refresh(location_db)
    return location_db

async def delete_location(location_id: int):
    location_db = session.query(Location).filter(Location.id == location_id).first()
    if location_db is None:
        raise HTTPException(status_code=404, detail="Location not found")
    session.delete(location_db)
    session.commit()
    return location_id

# User

async def create_user(user: UserSchema):
    if session.query(User).filter(User.name == user.name).first() is not None:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(
        name=user.name,
        password=user.password
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

async def read_users(username, password):
    if username is not None and password is not None:
        users = session.query(User).filter(User.name == username, User.password == password).all()
    elif username is not None:
        users = session.query(User).filter(User.name == username).all()
    elif password is not None:
        users = session.query(User).filter(User.password == password).all()
    else:
        users = session.query(User).all()
    return users

async def read_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def update_user(user_id: int, user: UserSchema):
    user_db = session.query(User).filter(User.id == user_id).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_db.name = user.name
    user_db.password = user.password
    session.commit()
    session.refresh(user_db)
    return user_db

async def delete_user(user_id: int):
    user_db = session.query(User).filter(User.id == user_id).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_db)
    session.commit()
    return user_id
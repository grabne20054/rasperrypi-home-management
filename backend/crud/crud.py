from api.model import WheaterDataSchema, LocationSchema, UserSchema
from db.session import session
from fastapi import HTTPException
from db.model import WheaterData, Location, User
from datetime import datetime, timedelta
from preprocessing.ProcessWheaterData import ProcessWheaterData
from collections import defaultdict

# WheaterData

async def create_wheater_data(wheater_data: WheaterDataSchema):
    preprocessed_wheater_data = ProcessWheaterData(wheater_data)
    if preprocessed_wheater_data.remove_false_values():
            
        new_wheater_data = WheaterData(
            temperature=wheater_data.temperature,
            humidity=wheater_data.humidity,
            wind_speed=wheater_data.wind_speed,
            timestamp=datetime.now() + timedelta(hours=2),
            rain_amount=wheater_data.rain_amount,
            location_id=wheater_data.location_id
        )
        if session.query(Location).filter(Location.id == new_wheater_data.location_id).first() is None:
            raise HTTPException(status_code=404, detail="Location not found")
        session.add(new_wheater_data)
        session.commit()
        session.refresh(new_wheater_data)
        return new_wheater_data
    else:
        raise HTTPException(status_code=400, detail="Invalid WheaterData")

async def read_wheater_data():
    daily_wheater_data = defaultdict(lambda: {'temperature': [], 'humidity': [], 'wind_speed': [], 'rain_amount': []})


    wheater_data = session.query(WheaterData).all()

    for data in wheater_data:
        timestamp = data.timestamp.strftime('%Y-%m-%d')
        daily_wheater_data[timestamp]['temperature'].append(data.temperature)
        daily_wheater_data[timestamp]['humidity'].append(data.humidity)
        daily_wheater_data[timestamp]['wind_speed'].append(data.wind_speed)
        daily_wheater_data[timestamp]['rain_amount'].append(data.rain_amount)

    averages = []
    for date, data in daily_wheater_data.items():
        avg_temp = sum(data['temperature']) / len(data['temperature']) if data['temperature'] else 0
        avg_humidity = sum(data['humidity']) / len(data['humidity']) if data['humidity'] else 0
        avg_wind_speed = sum(data['wind_speed']) / len(data['wind_speed']) if data['wind_speed'] else 0
        avg_rain_amount = sum(data['rain_amount']) / len(data['rain_amount']) if data['rain_amount'] else 0
        
        averages.append({
            'timestamp': date,
            'temperature': avg_temp,
            'humidity': avg_humidity,
            'wind_speed': avg_wind_speed,
            'rain_amount': avg_rain_amount
        })

    return averages


async def read_wheater_data_last_seven_days():
    daily_wheater_data = defaultdict(lambda: {'temperature': [], 'humidity': [], 'wind_speed': [], 'rain_amount': []})


    wheater_data = session.query(WheaterData).filter(WheaterData.timestamp > datetime.now() - timedelta(days=7)).all()

    for data in wheater_data:
        timestamp = data.timestamp.strftime('%Y-%m-%d')
        daily_wheater_data[timestamp]['temperature'].append(data.temperature)
        daily_wheater_data[timestamp]['humidity'].append(data.humidity)
        daily_wheater_data[timestamp]['wind_speed'].append(data.wind_speed)
        daily_wheater_data[timestamp]['rain_amount'].append(data.rain_amount)

    averages = []
    for date, data in daily_wheater_data.items():
        avg_temp = sum(data['temperature']) / len(data['temperature']) if data['temperature'] else 0
        avg_humidity = sum(data['humidity']) / len(data['humidity']) if data['humidity'] else 0
        avg_wind_speed = sum(data['wind_speed']) / len(data['wind_speed']) if data['wind_speed'] else 0
        avg_rain_amount = sum(data['rain_amount']) / len(data['rain_amount']) if data['rain_amount'] else 0
        
        averages.append({
            'timestamp': date,
            'temperature': avg_temp,
            'humidity': avg_humidity,
            'wind_speed': avg_wind_speed,
            'rain_amount': avg_rain_amount
        })

    return averages

async def read_wheater_data_last_day():
    wheater_data = session.query(WheaterData).filter(WheaterData.timestamp > datetime.now() - timedelta(days=1)).all()
    return wheater_data

async def read_wheater_data_location(location_id: int):
    wheater_data = session.query(WheaterData).filter(WheaterData.location_id == location_id).all()
    return wheater_data

async def read_wheater_data_location_last_entry(location_id: int):
    wheater_data = session.query(WheaterData).filter(WheaterData.location_id == location_id).order_by(WheaterData.timestamp.desc()).first()
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

async def delete_all_wheater_data():
    session.query(WheaterData).delete()
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
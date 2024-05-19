from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Double
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class WheaterData(Base):
    __tablename__ = "wheater_data"

    id = Column(Integer, primary_key=True)
    temperature = Column(Double)
    humidity = Column(Double)
    wind_speed = Column(Double)
    rain_amount = Column(Double)
    timestamp = Column(DateTime, default=datetime.now)
    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship("Location", back_populates="wheater_data")


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    latitude = Column(Double)
    longitude = Column(Double)
    wheater_data = relationship("WheaterData", back_populates="location")
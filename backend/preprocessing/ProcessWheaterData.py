import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from api.model import WheaterDataSchema

class ProcessWheaterData:
    def __init__(self, schema):
        if str(type(schema)) == "<class 'api.model.WheaterDataSchema'>":
            self.schema = schema
        else:
            raise Exception("Invalid schema type")
        
    def remove_false_values(self):
        if self.schema.temperature > 60.0:
            print("Invalid temperature: ", self.schema.temperature)
            return False
        elif self.schema.humidity < 0.0 or self.schema.humidity > 100.0:
            print("Invalid humidity: ", self.schema.humidity)
            return False
        elif self.schema.wind_speed < 0.0 or self.schema.wind_speed > 200.0:
            print("Invalid wind speed: ", self.schema.wind_speed)
            return False
        elif self.schema.rain_amount < 0.0 or self.schema.rain_amount > 100.0:
            print("Invalid rain amount: ", self.schema.rain_amount)
            return False
        return True
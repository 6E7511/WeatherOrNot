import cities
import weather_static
import json


class Weather:
    def __init__(self, city, dev):
        data = weather_static.query_weather(city, dev)
        self.city = city
        self.temp = round(data["main"]["temp"] - 273.15, 2)
        self.current_weather = data["weather"][0]["main"]
        self.clouds = data["clouds"]["all"]
        if "rain" in data:
            self.downfall_typ = "rain"
            if "1h" in data["rain"]:
                self.downfall_time = "1h"
            else:
                self.downfall_time = "3h"
            self.has_downfall = True
        elif "snow" in data:
            self.downfall_typ = "snow"
            if "1h" in data["snow"]:
                self.downfall_time = "1h"
            else:
                self.downfall_time = "3h"
            self.has_downfall = True
        else:
            self.has_downfall = False
        if self.has_downfall:
            self.downfall = data[self.downfall_typ][self.downfall_time]
            self.downfall_typ = self.downfall_typ.replace("s", "S")
            self.downfall_typ = self.downfall_typ.replace("r", "R")
        self.humidity = data["main"]["humidity"]
        self.wind_speed = data["wind"]["speed"]
        self.wind_deg_num = data["wind"]["deg"]
        if 22.5 < self.wind_deg_num <= 67.5:
            self.wind_deg_char = "NE"
        elif 67.5 < self.wind_deg_num <= 112.5:
            self.wind_deg_char = "E"
        elif 112.5 < self.wind_deg_num <= 157.5:
            self.wind_deg_char = "SE"
        elif 157.5 < self.wind_deg_num <= 202.5:
            self.wind_deg_char = "S"
        elif 202.5 < self.wind_deg_num <= 247.5:
            self.wind_deg_char = "SW"
        elif 247.5 < self.wind_deg_num <= 292.5:
            self.wind_deg_char = "W"
        elif 292.5 < self.wind_deg_num <= 337.5:
            self.wind_deg_char = "NW"
        else:
            self.wind_deg_char = "N"
        self.sunrise = data["sys"]["sunrise"]
        self.sunset = data["sys"]["sunset"]

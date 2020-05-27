from urllib.request import urlopen
from urllib.error import HTTPError
import json
import cities
import weather_obj
import datetime


url_base = "https://api.openweathermap.org/data/2.5/weather?q="
weather_key = "e71a27566a8253dbfd8169b0d0efb8ee"


def query_city(city_name, country_code):
    city_name = city_name.replace(" ", "+")
    city_name = city_name.replace("ü", "ue")
    city_name = city_name.replace("ö", "oe")
    city_name = city_name.replace("ä", "ae")
    url_final = url_base + city_name + "," + country_code + "&appid=" + weather_key
    try:
        data = json.load(urlopen(url_final))
        return cities.City(data["name"], data["sys"]["country"])
    except HTTPError:
        print("Error 404")      # TODO GUI response to error 404
        return 0


def query_weather(city, dev):
    name = city.name.replace(" ", "+")
    url_final = url_base + name + "," + city.country_code + "&appid=" + weather_key
    if dev:
        print(url_final)
    return json.load(urlopen(url_final))


def build_weather(weather):
    string = "Name : " + weather.city.name + "\nCountry : " + weather.city.country_code + \
             "\nCurrent weather : " + weather.current_weather + "\nTemperature : " + str(weather.temp) + "\nClouds : " \
             + str(weather.clouds) + " %" + "\n"
    if weather.has_downfall:
        string += weather.downfall_typ + " in last" + weather.downfall_time + " : " + str(weather.downfall) + "\n"
    string += "Wind speed : " + str(weather.wind_speed) + "m/s\n"
    string += "Wind direction : " + str(weather.wind_deg_num) + "°" + weather.wind_deg_char + "\n"
    string += "Humidity : " + str(weather.humidity) + " %\n"
    string += "Sunrise : " + str(datetime.datetime.fromtimestamp(weather.sunrise).strftime('%H:%M:%S')) + "\n"
    string += "Sunset : " + str(datetime.datetime.fromtimestamp(weather.sunset).strftime('%H:%M:%S')) + "\n"
    return string



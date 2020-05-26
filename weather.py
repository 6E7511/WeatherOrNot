from urllib.request import urlopen
from urllib.error import HTTPError
import json
import cities


url_base = "https://api.openweathermap.org/data/2.5/weather?q="
weather_key = "e71a27566a8253dbfd8169b0d0efb8ee"


def query_city(city_name, country_code):
    city_name = city_name.replace(" ", "+")
    url_final = url_base + city_name + "," + country_code + "&appid=" + weather_key
    try:
        data = json.load(urlopen(url_final))
        return cities.City(data["name"], data["sys"]["country"])
    except HTTPError:
        print("Error 404")
        return 0


def query_weather(city, dev):
    name = city.name.replace(" ", "+")
    url_final = url_base + name + "," + city.country_code + "&appid=" + weather_key
    if dev:
        print(url_final)
    return json.load(urlopen(url_final))


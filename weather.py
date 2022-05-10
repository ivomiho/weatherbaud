from tkinter import *
import requests
import math


city_name = "Cordoba,AR"
api_key = "240b7085cdf607291959db06dc7283ad"

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url).json()
    
    temp = response["main"]["temp"]
    temp = math.floor((temp * 1.8) - 459.67)
    
    feels_like = response["main"]["feels_like"]
    feels_like = math.floor((temp * 1.8) - 459.67)
    
    humidity = response["main"]["humidity"]
    
    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity    
    }
    
weather = get_weather(api_key, city_name)
print(weather)
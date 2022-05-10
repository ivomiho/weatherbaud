from typing import Optional
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl
import requests

app2 = FastAPI()

# api_key = "240b7085cdf607291959db06dc7283ad"
# city_name = "London"

@app2.get('/weather/{city}')
def get_weather(city: str):
     
     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=240b7085cdf607291959db06dc7283ad'.format(city)
     
     response = requests.get(url)
     
     data = response.json()
     
     name = data['name']
     
     print(response)
     print(data)
     print(name)
     
     return data
     
    


# # class Weather(BaseModel):
# #     id: str
# #     city: str
# #     celcius: float
# #     fahrenheit: float


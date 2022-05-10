import requests
# import pprint

city = input('Enter your city: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=240b7085cdf607291959db06dc7283ad'.format(city)

result = requests.get(url)

data = result.json()

temp = data['main']['temp']

print('Temperature: ', temp)
print('Temperature: {} degrees C'.format(temp))

# print(result)

# print(data)
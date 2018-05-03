import requests

api_address = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=777787647ba4bfe6f48fc4c17b1a5ef3&q='

city = input('City Name : ')

url = api_address + city

json_data = requests.get(url).json()

formatted_data = json_data['list'][0]['weather'][0]['description']

print('The weather right now is: ' + formatted_data)

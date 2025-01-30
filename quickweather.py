import requests
import sys
import json

# Get location from user input instead of sys.argv
location = input("Enter city/state name: ") 
# to store api key to secure it

url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=(Your api key)" % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
data = weatherData['weather']
print('current weather in %s:' % (location))
print(data[0]['main'], "-", data[0]['description'])

temp = weatherData['main']
print('temperature is:', temp['temp'] - 273.25, "C")
print()

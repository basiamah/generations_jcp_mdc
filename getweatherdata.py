#!usr/bin/env python3

# A Python program for getting weather data from
# Open Weather Map

APPID = 'd7ee7c665b2a683aef9f31263d37b730'

import json, requests, sys

# Get location from command line arguments
# python3 getweatherdata.py Miami, US

if len(sys.argv) < 2:
	print("Error: need to enter city name and 2-letter country code")
	sys.exit()
print("Success")

# create a string variable by joining all elements of the sys.argv list
# using the join method available in the string data type
print("Content of sys.argv list ")
print(sys.argv[1:])

location = ''.join(sys.argv[1:]) # City,CountryCode as a string
print('Location: ' + location)

# Download the JSON data from OpenWeatherMap.org's API
url ='https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APPID

# send requests to url and get response
response = requests.get(url)
response.raise_for_status()

# Uncomment the following to see the raw JSON Text:
# print(response.text)

# Load JSON data into a Python dictionary variable
weatherData = json.loads(response.text)
print(weatherData)
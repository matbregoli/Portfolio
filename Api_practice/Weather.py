import requests
import json
from LatLongSearcher import Lat_Long_Searcher
from Date_manager import date_manager

class WeatherAPI:
	
	def get_weather_in_address(self, address):

		lat_lon = Lat_Long_Searcher.search_by_address(address)

		parameters = {
			'lon' : lat_lon['lng'],
			'lat': lat_lon['lat'],
			'ac': '0',
			'unit': 'metric',
			'output': 'json',
			'tzshift': '0'
			}

		response = requests.get("https://www.7timer.info/bin/civillight.php", params = parameters)
		return response.json()['dataseries']

	def build_weathers(self, address):
		weathers = []
		weather_dics = self.get_weather_in_address(address)
		for weather in weather_dics:
			string_date = date_manager.dates_to_string(weather)
			new_weather = weather_date(date_manager.get_day(string_date), date_manager.get_date(string_date), weather['weather'], weather['temp2m']['max'], weather['temp2m']['min'])
			weathers.append(new_weather)
		return weathers

weatherAPI = WeatherAPI()

class weather_date:
	def __init__(self, day, date, weather, temp_max, temp_min):
		self.day = day
		self.date = date
		self.weather =weather
		self.temp_max = temp_max
		self.temp_min = temp_min

	def get_day(self):
		return self.day

	def get_date(self):
		return self.date

	def get_weather(self):
		return self.weather

	def get_temp_max(self):
			return self.temp_max

	def get_temp_min(self):
			return self.temp_min


weather_type_img = {
	'clear':"Clear.jpg", 
	'pcloudy':"Pcloudy.jpg",
	'mcloudy':"Cloudy.jpg",
	'cloudy':"Cloudy.jpg",
	'humid': "Cloudy.jpg",
	'lightrain':"Rain.jpg",
	'oshower': "Rain.jpg",
	'ishower':"Rain.jpg",
	'lightsnow': "Snow.jpg",
	'rain':"Rain.jpg",
	'snow':"Snow.jpg",
	'rainsnow':"Snow.jpg",
}

#print(weather_type_img['clear'])

#print(weatherAPI.get_weather_in_address('Pilar Buenos Aires Argentina')[0])

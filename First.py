import requests
import json
from LatLongSearcher import Lat_Long_Searcher

# parameters = {
# 	'lon' : '-58.449722',
# 	'lat': '-34.672',
# 	'ac': '0',
# 	'unit': 'metric',
# 	'output': 'json',
# 	'tzshift': '0'
# }

# response = requests.get("https://www.7timer.info/bin/civillight.php", params = parameters)

# def jprint(obj):
# 	text = json.dumps(obj, sort_keys=True, indent=4)
# 	return text

# print(response.json()['dataseries'][0])

class Weather:
	
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


weather = Weather()

print(weather.get_weather_in_address('Pilar Buenos Aires Argentina'))

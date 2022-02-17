import requests
import json

# def jprint(obj):
# 	text = json.dumps(obj, sort_keys=True, indent = 4)
	# return text

class LatLongSearcher:

	def search_by_address(self, address):
		#Returns a dic with lat and lng of a given address(First one found in API)
		parameters = {
			'key' : 'z5ArnnkxBe4Saxf5PwKhLowbtF9NvxFg',
			'location' : address,
			'outFormat' : 'json'
		}
		response = requests.get('http://www.mapquestapi.com/geocoding/v1/address', params = parameters)
		return response.json()['results'][0]['locations'][0]['displayLatLng']

Lat_Long_Searcher = LatLongSearcher()

# print(Lat_Long_Searcher.search_by_address('Pilar, Buenos Aires, Argentina'))
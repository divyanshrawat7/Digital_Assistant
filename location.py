# import requests
# import json

# send_url = "http://api.ipstack.com/check?access_key=3f61a6288e09da898b81d9dea45292fc"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']
# print(city)

from pprint import pprint
import googlemaps 

API_KEY ='AIzaSyCa-Immg-THl-N4gbIki0hHLm0aEMOIKJI'

map_client=googlemaps.Client (API_KEY)

work_place_address= '1 , Lane No. 5A, Sadbhawana Colony, Mohkampur, Dehradun, Uttarakhand 248005, India'
response = map_client.geocode (work_place_address)

pprint (response)
print (response[0]['geometry'])
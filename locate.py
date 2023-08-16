from statistics import geometric_mean
import phonenumbers
#from text import number
number="+919634141967"
#numbers='7668962069'
#country_code="+91"
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))
phno=phonenumbers.parse(number)
yourLocation=geocoder.description_for_number(phno,"en")
print(yourLocation)
from opencage.geocoder import OpenCageGeocode
key='c9d9765b2f8c4f778c9f093a36e5ed35'
geocoder=OpenCageGeocode(key)
qe=str(yourLocation)
results=geocoder.geocode(qe)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)


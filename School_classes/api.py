import requests
import json


#call openweathermap api
req = requests.get('http://api.openweathermap.org/data/2.5/onecall')

lat = 49.08
lon = 16.43

ip_request = requests.get('https://ip-api.com/json')
if ip_request.ok:
    ip_data = ip_request.json()
    lat = ip_data['lat']
    lon = ip_data['lon']

query_params = {
    'lat': lat,
    'lon': lon,
    'units': 'metric',
}

print(req.status_code)
print(req.headers['content-type'])
print(req.encoding)
print(req.text)


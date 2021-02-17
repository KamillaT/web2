import requests
import sys
from io import BytesIO
from PIL import Image
from set_params import set_geocoder_params


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
toponym_to_find = ' '.join(sys.argv[1:])
geocoder_params = set_geocoder_params(toponym_to_find)
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coords = ','.join(toponym["Point"]["pos"].split())
geocoder_params = set_geocoder_params(toponym_coords, kind="district")
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response_d = response.json()
toponym_d = json_response_d["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_address = toponym_d["metaDataProperty"]["GeocoderMetaData"]["text"]
print(toponym_address)

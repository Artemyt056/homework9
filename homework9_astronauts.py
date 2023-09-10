import requests
from pprint import pprint

url = 'http://api.open-notify.org/astros.json'

astronauts_in_space = requests.get(url)

astronauts = astronauts_in_space.json()
pprint(astronauts)

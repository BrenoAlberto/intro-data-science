import json
import requests

url = 'http://api.wunderground.com/api/36ad6818334522c0/conditions/q/NY/newyork.json'
data = requests.get(url).text
data = json.loads(data)

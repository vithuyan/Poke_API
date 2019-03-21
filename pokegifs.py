import json
import requests
import os
res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"])

key = os.environ.get("GIPHY_KEY")
q = "pikachu"
rating = "g"


url = "https://api.giphy.com/v1/gifs/search?api_key={giphy_key}=pikachu&rating=g".format(key)
requests.get(url)
print(url)

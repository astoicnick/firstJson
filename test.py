import requests as r
import json

API_KEY = "XXXXX"
KEYWORD = "Rick and Morty"
skywalker = (r.get("https://www.googleapis.com/youtube/v3/search?part=snippet&q="+ KEYWORD +"&key="+API_KEY)).json()

for item  in skywalker['items']:
    #Parse through data like this
    print(item['id']['videoId'])

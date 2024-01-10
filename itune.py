import requests
import sys
import json

if len(sys.argv) != 3:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1] + sys.argv[2])

o = response.json()
for result in o["results"]:
    print(result["trackName"])


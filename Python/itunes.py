import json
import requests
import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
o = response.json()

track = o["results"][0]["trackName"]

for result in o["results"]:
    print(result["trackName"])

# print(json.dumps(response.json(), indent=2)) 
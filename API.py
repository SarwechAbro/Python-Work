import json
import requests
import sys
if len(sys.argv) !=2:
    sys.exit()


res = requests.get("https://itunes.apple.com/search?entity=song&limit=1000&term="+sys.argv[1])
o = res.json()
for result in o["results"]:
    print(result["trackName"])
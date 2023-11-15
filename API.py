import json
import requests
import sys

if len(sys.argv)!=2: #weezer
    sys.exit()

res = requests.get("https://itunes.apple.com/search?entity=song&liit=50&term="+sys.argv[1])
o = res.json()



for result in o["results"]:
   print(result["trackNumber"],result["trackName"])


  
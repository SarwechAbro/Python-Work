import json
import requests
import sys

res = requests.get("https://www.amdoren.com/api/currency.php")
o = res.json()
print(0)
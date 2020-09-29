import requests
import re
import json

url = "http://localhost:3000"
data = {"msg":'hello'}
headers ={'Content-type':'application/json','Accept':'text/plain'}




r = requests.post(url,data=json.dumps(data),headers=headers)


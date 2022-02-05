from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# class handler(BaseHTTPRequestHandler):

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/python'
r = requests.get(url)
data = r.json()
# print(data)
def_list = data
# for item in data:
#     print(item)
definition = data["meanings"][0]["definitions"][0]["definition"]
print(str(definition))
# definitions = []
# for word_data in data:
#     definition = word_data["meanings"][0]["definitions"][0]["definition"]
#     definitions.append(definition)
# message = str(definitions)        




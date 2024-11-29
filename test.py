import requests
import json
import rich

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# response is a Response object (object created by requests module) not a python object
# to be specific its a reqeusts.models.Response object..
print(response)
print(type(response))

# to convert this Response object we get from reqeuest.. we need a specifi method called .json()
# this .json() methods works only (as far I know) on response objects
# response.json() converts Response object to python object (ex: dict, or list)
data = response.json()

# OUTPUTTING THE DATA

# 1. to print in a colorful and more readable format..
# rich.print_json(data=data)


# 2. USING JSON.DUMPS TO CREATE A JSON_FORMAT_STRING. (easy to read)
# json.dumps .dumps is a json method that takes a python object and converts it to JSON
json_string = json.dumps(data, indent=2)
print(json_string)

# challenge get the usssd rate of bitcoin
rate = data['bpi']['USD']['rate']
rate_float = data['bpi']['USD']['rate_float']
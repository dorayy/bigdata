import requests
import json

flights = "https://airlabs.co/api/v9/flights?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
delays_departures = "https://airlabs.co/api/v9/delays?delay=30&type=departures&api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
delays_arrivals = "https://airlabs.co/api/v9/delays?delay=30&type=arrivals&api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
airlines = "https://airlabs.co/api/v9/airlines?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
airports = "https://airlabs.co/api/v9/airports?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
cities = "https://airlabs.co/api/v9/cities?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
fleets = "https://airlabs.co/api/v9/fleets?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"
contries = "https://airlabs.co/api/v9/countries?api_key=77bb8ae0-0df8-49f3-9183-727e4ca781ef"

payload={}
headers = {}

response = requests.request("GET", flights, headers=headers, data=payload)
response = response.json()
response = response['response']

response2 = requests.request("GET", delays_departures, headers=headers, data=payload)
response2 = response2.json()
response2 = response2['response']

response3 = requests.request("GET", delays_arrivals, headers=headers, data=payload)
response3 = response3.json()
response3 = response3['response']

response4 = requests.request("GET", airlines, headers=headers, data=payload)
response4 = response4.json()
response4 = response4['response']

response5 = requests.request("GET", airports, headers=headers, data=payload)
response5 = response5.json()
response5 = response5['response']

response6 = requests.request("GET", cities, headers=headers, data=payload)
response6 = response6.json()
response6 = response6['response']

response7 = requests.request("GET", fleets, headers=headers, data=payload)
response7 = response7.json()
response7 = response7['response']

response8 = requests.request("GET", contries, headers=headers, data=payload)
response8 = response8.json()
response8 = response8['response']


# save json to file
with open('/root/data/flights.json', 'w') as outfile:
    json.dump(response, outfile)

with open('/root/data/delays_departures.json', 'w') as outfile:
    json.dump(response2, outfile)

with open('/root/data/delays_arrivals.json', 'w') as outfile:
    json.dump(response3, outfile)

with open('/root/data/airlines.json', 'w') as outfile:
    json.dump(response4, outfile)

with open('/root/data/airports.json', 'w') as outfile:
    json.dump(response5, outfile)

with open('/root/data/cities.json', 'w') as outfile:
    json.dump(response6, outfile)

with open('/root/data/fleets.json', 'w') as outfile:
    json.dump(response7, outfile)

with open('/root/data/contries.json', 'w') as outfile:
    json.dump(response8, outfile)
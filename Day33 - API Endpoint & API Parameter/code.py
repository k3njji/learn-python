import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# print(data)

req = {
    'lat': -51.3994,
    'lng': 93.1786,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=req)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

dntR = sunrise.split('T')
dntS = sunset.split('T')

print(dntR, dntS)

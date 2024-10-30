from multiprocessing.connection import Client

import requests

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "api key"

accountSid = "account id"
authToken = "tpken"

weather_params = {
    "lat" : "your latitude",
    "lon" : "your longitude",
    "appid" :api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(accountSid, authToken)
    message = client.messages \
       .create(
        body = 'Its going to rain today. remember to bring an umbrella',
        from = 'created number',
        to = 'to your number'
    )
    .then(message => console.log(message.sid));

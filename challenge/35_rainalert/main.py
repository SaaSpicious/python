import requests
from twilio.rest import Client

MY_LAT = 48.483334
MY_LONG = 9.216667

def send_message():
    with open("codes/twilio_account_id.txt","r") as file:
        twilio_account_id = file.read()
    with open("codes/twilio_auth_key.txt", "r") as file:
        twilio_auth_key = file.read()
    with open("codes/phonenumber.txt", "r") as file:
        phone_number = file.read()
    twilio_client = Client(twilio_account_id,twilio_auth_key)
    twilio_message = twilio_client.messages.create(
        body = "It's going to rain, please bring an umbrella!",
        from_ = 'whatsapp:+14155238886',
        to = f'whatsapp:{phone_number}'
    )
    print(twilio_message.status)


with open("codes/open_weather_api_key.txt", "r") as file:
    api_key = file.read()

api_url = "https://api.openweathermap.org/data/2.5/forecast"
api_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 12
}

api_call = requests.get(url=api_url,params=api_params)

weather_data = api_call.json()["list"]


it_will_rain=False
for weather in weather_data:
    if int(weather["weather"][0]["id"]) < 700: # Check for weather condition that implies rain
        it_will_rain=True
        break

if it_will_rain:
    print("Bring an umbrella!")
    send_message()



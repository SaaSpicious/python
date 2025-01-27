import requests
from datetime import datetime

MY_LAT = 48.483334
MY_LONG = 9.216667

def get_iss_position():
    api_url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url=api_url)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = {
        "lat": iss_latitude,
        "lng": iss_longitude
    }
    return iss_position


def check_if_iss_in_range(iss_position,your_position):
    if abs(iss_position["lng"] - your_position["lng"]) < 5 and abs(iss_position["lat"] - your_position["lat"]) < 5:
        return True
    else:
        return False


def check_if_dark(parameters):
    api_url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url=api_url, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

iss_position=get_iss_position()

if check_if_iss_in_range(iss_position,parameters):
    print("ISS is currently close to you!")
    if check_if_dark(parameters):
        print("It's dark as fuck where you currently at!")
        print("Look up at the sky my friend...")
    else:
        print("Nope, too bright to see the ISS, sorry...")
else:
    print("ISS is currently too far away, sorry mate!")
    print(f"ISS is currently here: {iss_position}")
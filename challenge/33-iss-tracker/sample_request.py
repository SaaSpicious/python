import requests
from datetime import datetime

MY_LAT = 48.483334
MY_LONG = 9.216667

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code == 404:
    raise Exception("Resource doesn't exist")
elif response.status_code == 403:
    raise Exception("You're not authorized to access his resource")
elif response.status_code != 200:
    raise Exception(f"Unknown error occurred. Response code {response.status_code}")
elif response.status_code == 200:
    print(response.json()["iss_position"])



request_params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=request_params)
print(response.status_code)
print(response.json())

sunrise_hr = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
current_time = str(datetime.now()).split(" ")[1].split(":")[0]

print(current_time,sunrise_hr,sunset_hr)
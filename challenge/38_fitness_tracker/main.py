from datetime import datetime
import requests


CREDENTIALS_FILE="credentials/api_credentials.cred"

def get_api_keys(credentials_file):
    api_keys = {}
    file = open(credentials_file, "r")
    lines = file.readlines()
    for line in lines:
        list = line.split("=")
        key = list[0].strip()
        value = list[1].strip()
        api_keys[key]=value
    return api_keys

def get_exercise_api_response(exercise_input,credentials):
    exercise_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    exercise_api_header = {
        "Content-Type": "application/json",
        "x-app-id": credentials["NUTRITIONIX_APP_ID"],
        "x-app-key": credentials["NUTRITIONIX_API_KEY"]
    }

    exercise_api_body = {
        "query": exercise_input
    }

    response = requests.post(url=exercise_api_endpoint, json=exercise_api_body, headers=exercise_api_header)
    return response.json()

def post_exercise_to_sheet(exercise,credentials):
    sheety_api_endpoint = f"https://api.sheety.co/{credentials["SHEETY_USERNAME"]}/myWorkouts/workouts"
    sheety_api_header = {
        "Authorization": f"Bearer {credentials["SHEETY_BEARER_TOKEN"]}"
    }

    current_day = datetime.now().strftime("%d.%m.%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    sheety_api_body = {
        "workout": {
            "date": current_day,
            "time": current_time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    print(sheety_api_body)

    response = requests.post(url=sheety_api_endpoint, json=sheety_api_body, headers=sheety_api_header)
    return response.status_code


exercise_input = str(input("What did you do today? "))

exercise_api_response = get_exercise_api_response(exercise_input,get_api_keys(CREDENTIALS_FILE))
print(exercise_api_response)

sheety_api_response = post_exercise_to_sheet(exercise_api_response["exercises"][0],get_api_keys(CREDENTIALS_FILE))
print(sheety_api_response)
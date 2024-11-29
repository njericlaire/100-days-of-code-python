from time import strftime

import requests
from datetime import datetime

today=datetime.now()
day=today.strftime("%d/%m/%Y")
exe_time=strftime("%H.%M.%S")
print(day)

API_KEY="2013ff188dfcdc138e6a476232fdccee"
APP_ID="7c1451ef"
GENDER = "Female"
WEIGHT_KG = 80
HEIGHT_CM = 186
AGE = 20

exercise=input("What exersice have you done today? ")

headers={
"x-app-id":APP_ID,
"x-app-key":API_KEY
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exersice_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(exersice_endpoint, json=parameters, headers=headers)
result = response.json()
exe=result['exercises'][0]
exe_type=exe['user_input']
exe_duration=exe['duration_min']
exe_calories=exe['nf_calories']

sheet_parameters = {
    "workout": {
        "Date": day,
        "Time": exe_time,
        "Exercise": exe_type,
        "Duration": exe_duration,
        "Calories": exe_calories
    }
}

sheet_response=requests.post(url="https://api.sheety.co/470730c7d1bcaedc9a1a66f8bbcbc137/workoutTracking/workouts",json=sheet_parameters)
print(sheet_response.text)
print(result)


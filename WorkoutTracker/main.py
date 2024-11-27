import requests


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
print(result)


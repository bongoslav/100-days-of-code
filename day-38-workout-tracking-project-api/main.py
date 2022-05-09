import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 183
AGE = 22
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
TODAY_DATE = datetime.today().strftime("%d/%m/%Y")
TIME_NOW = datetime.now().strftime("%X")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/629647644d353f34d535f846cfd84c81/workoutTracking100DaysOfCode/workouts"

user_input = input("Tell me which exercises you did: ")

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(exercise_endpoint, json=exercise_parameters, headers=exercise_headers)
result_exercise = response.json()

sheety_parameters = {
    "workout": {
        "date": TODAY_DATE,
        "time": TIME_NOW,
        "exercise": result_exercise["exercises"][0]['name'].title(),
        "duration": result_exercise["exercises"][0]["duration_min"],
        "calories": result_exercise["exercises"][0]["nf_calories"],
    }
}
response = requests.post(sheety_endpoint, json=sheety_parameters, auth=(USERNAME, PASSWORD))
result = response.json()
print(result)
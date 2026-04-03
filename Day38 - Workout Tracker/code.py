import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

NUTRITION_API_KEY = os.getenv("NUTRITION_APP_KEY")
NUTRITION_API_ID = os.getenv("NUTRITION_APP_ID")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")   # optional if your sheet requires auth

BASE_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_URL = "https://api.sheety.co/9a72066ca1c652fc6b3ce27fc02a4b70/worksheetTrackerPython/sheet1"

nutrition_headers = {
    "x-app-id": NUTRITION_API_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json"
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
} if SHEETY_TOKEN else {}

query = {
    "query": input("What exercise did you do? ")
}

if input("Do you want to input the details (Yes/No)? ").lower() == "yes":
    query["weight_kg"] = int(input("Input your weight: "))
    query["height_cm"] = int(input("Input your height: "))
    query["age"] = int(input("Input your age: "))
    query["gender"] = input("Input your gender: ")

response = requests.post(BASE_URL, json=query, headers=nutrition_headers)
response.raise_for_status()

data = response.json()

now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in data["exercises"]:

    sheet_input = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_URL,
        json=sheet_input,
        headers=sheety_headers
    )

    sheet_response.raise_for_status()
    print(sheet_response.json())
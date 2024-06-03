from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="libreville"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    response = requests.get(request_url).json()
    return response


    


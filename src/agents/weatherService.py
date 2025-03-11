from typing import Dict, Union
import random
from datetime import datetime

# def fetch_weather_data(location):
#     """Fetch weather data for a given location."""
#     import requests
#     import os

#     api_key = os.getenv("WEATHER_API_KEY")
#     base_url = "http://api.openweathermap.org/data/2.5/weather"

#     params = {
#         'q': location,
#         'appid': api_key,
#         'units': 'metric'  # Use 'imperial' for Fahrenheit
#     }

#     response = requests.get(base_url, params=params)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

capitals = {
    "London": {"country": "UK", "base_temp": 15},
    "Paris": {"country": "France", "base_temp": 18},
    "Berlin": {"country": "Germany", "base_temp": 16},
    "Tokyo": {"country": "Japan", "base_temp": 22},
    "Washington": {"country": "USA", "base_temp": 20},
    "Moscow": {"country": "Russia", "base_temp": 12},
    "Beijing": {"country": "China", "base_temp": 19},
    "Rome": {"country": "Italy", "base_temp": 23},
}

def fetch_weather_data(location):
    """Fetch weather data for a given location."""
    
    location = location.replace('\n','').replace('`','')
    if location not in capitals:
        return f"Location {location} not found in database"
        # raise ValueError(f"Location {location} not found in database")
    
    # Generate random variation (-5 to +5) from base temperature
    base_temp = capitals[location]["base_temp"]
    variation = random.uniform(-5, 5)
    current_temp = round(base_temp + variation, 1)
    
    # Add seasonal adjustment based on current month
    month = datetime.now().month
    # Northern hemisphere seasonal adjustment
    if location not in ["Beijing", "Tokyo"]:  
        if 3 <= month <= 5:  # Spring
            current_temp += 5
        elif 6 <= month <= 8:  # Summer
            current_temp += 10
        elif 9 <= month <= 11:  # Autumn
            current_temp -= 3
        else:  # Winter
            current_temp -= 8
    
    response = {
        "city": location,
        "country": capitals[location]["country"],
        "temperature": current_temp,
        "unit": "Celsius",
        "timestamp": datetime.now().isoformat()
    }

    return response
    
def process_weather_data(data):
    """Process the weather data and extract relevant information."""
    if data:
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]

        temperature = main.get('temp')
        description = weather.get('description')

        return {
            'temperature': temperature,
            'description': description
        }
    return None
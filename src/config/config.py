# File: /weather-agent/weather-agent/src/config/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings
class Config:
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    BASE_URL = os.getenv("BASE_URL", "https://api.weatherapi.com/v1")  # Default base URL
    TIMEOUT = int(os.getenv("TIMEOUT", 10))  # Default timeout in seconds
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Default log level

import os

# Configuration for OpenWeatherMap API
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key")
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
FETCH_INTERVAL = 300  # in seconds (5 minutes)

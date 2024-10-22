import requests
from models import WeatherData
from datetime import datetime

def fetch_weather_data(app, db):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    api_key = app.config['OPENWEATHER_API_KEY']

    with app.app_context():
        for city in cities:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
                feels_like = data['main']['feels_like'] - 273.15
                main_condition = data['weather'][0]['main']
                timestamp = datetime.utcfromtimestamp(data['dt'])

                weather = WeatherData(
                    city=city,
                    temperature=temperature,
                    feels_like=feels_like,
                    main_condition=main_condition,
                    timestamp=timestamp
                )

                db.session.add(weather)
                db.session.commit()

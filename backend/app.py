from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from weather_scheduler import fetch_weather_data
import os

app = Flask(__name__)
CORS(app)

# Load environment variable for OpenWeather API key
app.config['OPENWEATHER_API_KEY'] = os.getenv('OPENWEATHER_API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import WeatherData

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve weather data
@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    weather_records = WeatherData.query.all()
    data = [{
        "city": record.city,
        "temperature": record.temperature,
        "feels_like": record.feels_like,
        "main_condition": record.main_condition,
        "timestamp": record.timestamp
    } for record in weather_records]
    return jsonify(data)

# Scheduler to fetch weather data periodically
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_weather_data, trigger="interval", minutes=5, args=[app, db])
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from app import db

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    feels_like = db.Column(db.Float, nullable=False)
    main_condition = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

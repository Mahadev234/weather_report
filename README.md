# Weather Monitoring System

## Overview
This project is a **Real-Time Weather Monitoring System** that fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/), processes it to provide summarized insights (such as average, maximum, and minimum temperature), and triggers alerts if certain thresholds are breached (e.g., high temperature). The system displays real-time weather data for major Indian cities, including visualizations and alerts.

The project is built with a **React.js** frontend styled using **Tailwind CSS**, and a **Python Flask** backend that communicates with the **OpenWeatherMap API** and manages data processing. A **SQLite** database is used for storing weather data summaries.

## Features
- Real-time weather data for Indian metros: Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad.
- Data aggregation with daily summaries, including:
  - Average temperature.
  - Maximum temperature.
  - Minimum temperature.
  - Dominant weather condition.
- User-configurable temperature alert system.
- Historical weather trends (to be visualized).
- RESTful API for frontend-backend communication.
- Responsive and clean UI built with Tailwind CSS.

---

## System Architecture

### **Frontend (React.js + Tailwind CSS)**
- **React.js**: Used for rendering UI components, fetching backend data, and managing application state.
- **Tailwind CSS**: Applied for styling the application with utility-first CSS classes.
- **Chart.js + react-chartjs-2**: Used for visualizing historical weather data (future enhancement).
  
### **Backend (Flask)**
- **Python Flask**: A lightweight web framework for setting up APIs and scheduling background jobs for periodic weather data fetching.
- **APScheduler**: Used for scheduling periodic jobs to fetch weather data from the OpenWeatherMap API at configurable intervals (every 5 minutes by default).
- **SQLite Database**: Used to store fetched weather data and daily aggregates.
- **Flask-SQLAlchemy**: ORM for managing database interactions.

---

## Requirements and Dependencies

### **Frontend (React.js + Tailwind CSS)**
- **Node.js** and **npm**: To build and run the React.js application.
- **Tailwind CSS**: For styling the frontend components.
- **axios**: For making HTTP requests to the Flask backend.
- **Chart.js** and **react-chartjs-2**: For data visualization (optional).

### **Backend (Python + Flask)**
- **Python 3.x**: Backend development with Flask.
- **Flask**: For handling API requests and rendering data.
- **Flask-CORS**: To allow cross-origin requests from the React frontend.
- **Flask-SQLAlchemy**: ORM for database interaction.
- **APScheduler**: For background jobs (periodic weather data fetching).
- **SQLite**: Lightweight database to store weather data.

### **Docker/Podman**
For an isolated setup using Docker containers, the backend and frontend can be containerized. Below are Docker configurations for each service.

---

## Build Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/weather-monitoring-system.git
cd weather-monitoring-system
```

### 2. Set up Environment Variables

You need an API key from OpenWeatherMap. Create an environment variable for it.

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

### 3. Backend (Python Flask) Setup

#### a. Using Docker (Recommended)
- Ensure **Docker** or **Podman** is installed.
- Build the Docker image:
  ```bash
  cd weather-monitoring-backend
  docker build -t weather-backend .
  ```
- Run the Flask server container:
  ```bash
  docker run -d -p 5000:5000 --env OPENWEATHER_API_KEY="your_api_key_here" weather-backend
  ```
- This will launch the Flask backend on `http://localhost:5000`.

#### b. Manual Setup (without Docker)
- Create a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Initialize the SQLite database:
  ```bash
  python app.py
  ```
- Flask server will run on `http://localhost:5000`.

---

### 4. Frontend (React) Setup

#### a. Using Docker
- Build the frontend Docker image:
  ```bash
  cd weather-monitoring-frontend
  docker build -t weather-frontend .
  ```
- Run the React frontend container:
  ```bash
  docker run -d -p 3000:3000 weather-frontend
  ```
- The frontend will be accessible at `http://localhost:3000`.

#### b. Manual Setup (without Docker)
- Install the required dependencies:
  ```bash
  npm install
  ```
- Start the React development server:
  ```bash
  npm start
  ```
- The frontend will be accessible at `http://localhost:3000`.

---

## Design Choices

1. **React.js with Tailwind CSS**: 
   - **React** was chosen for its component-based architecture, enabling efficient updates and re-rendering of the user interface.
   - **Tailwind CSS** allows for rapid styling using utility classes without the need for custom CSS for most components.
  
2. **Flask (Python)**:
   - **Flask** is lightweight and well-suited for small to medium-sized applications where performance is critical. It allows for easy API creation and integration with background services like APScheduler for periodic jobs.

3. **SQLite**:
   - Chosen for simplicity as the data volume (weather data) is relatively small, and the structure is easily managed by SQLite without needing the overhead of a full database system.

4. **APScheduler**:
   - Used to schedule background jobs that periodically fetch weather data every 5 minutes. This ensures real-time updates are captured and aggregated properly.

5. **Docker**:
   - Docker is used to isolate both frontend and backend environments, ensuring consistency across different systems and simplifying deployment.

---

## Testing Instructions

### Frontend
1. Run the React frontend using `npm start`.
2. Ensure weather data is fetched from the backend API and displayed correctly in the UI.
3. Test the responsiveness of the application across different screen sizes (Tailwind CSS ensures mobile-first design).

### Backend
1. Ensure Flask connects to the OpenWeatherMap API correctly by checking the `http://localhost:5000/api/weather` endpoint.
2. Check that weather data is stored in the database.
3. Simulate alert thresholds by modifying temperature data and ensuring alerts are triggered.

---

## Future Enhancements
1. **Historical Trends Visualization**: Add support for weather data trend graphs using Chart.js.
2. **User Authentication**: Allow users to save their custom alert preferences.
3. **Weather Forecasts**: Extend the backend to fetch and display future weather forecasts.
4. **Scaling the System**: Move from SQLite to a production-grade database like PostgreSQL when scaling.

---

## License
This project is licensed under the MIT License.


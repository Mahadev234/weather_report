import React, { useState, useEffect } from 'react';
import axios from 'axios';
import WeatherCard from './components/WeatherCard';
import Alerts from './components/Alerts';

const App = () => {
  const [weatherData, setWeatherData] = useState([]);
  const [alert, setAlert] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/weather')
      .then((response) => setWeatherData(response.data))
      .catch((error) => console.error(error));
  }, []);

  useEffect(() => {
    const latestData = weatherData[0];
    if (latestData && latestData.temperature > 35) {
      setAlert(`Alert: High temperature in ${latestData.city}`);
    }
  }, [weatherData]);

  return (
    <div className="container mx-auto p-5">
      <h1 className="text-4xl font-bold mb-5 text-center">Weather Monitoring Dashboard</h1>
      {alert && <Alerts alertMessage={alert} />}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {weatherData.map((data, index) => (
          <WeatherCard key={index} data={data} />
        ))}
      </div>
    </div>
  );
};

export default App;

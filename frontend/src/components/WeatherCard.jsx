import React from 'react';

const WeatherCard = ({ data }) => {
    return (
        <div className="bg-white shadow-md rounded-lg p-4">
            <h2 className="text-xl font-bold">{data.city}</h2>
            <p>Temperature: {data.temperature.toFixed(1)}°C</p>
            <p>Feels Like: {data.feels_like.toFixed(1)}°C</p>
            <p>Main Condition: {data.main_condition}</p>
            <p>Timestamp: {new Date(data.timestamp).toLocaleString()}</p>
        </div>
    );
};

export default WeatherCard;

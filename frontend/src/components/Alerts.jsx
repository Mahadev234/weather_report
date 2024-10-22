import React from 'react';

const Alerts = ({ alertMessage }) => {
    return (
        <div className="bg-red-200 p-4 mt-5">
            <h2 className="text-2xl font-bold">Alert</h2>
            <p>{alertMessage}</p>
        </div>
    );
};

export default Alerts;

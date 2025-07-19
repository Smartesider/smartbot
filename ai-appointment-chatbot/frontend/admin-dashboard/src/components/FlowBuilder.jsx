import React, { useState } from 'react';

const FlowBuilder = () => {
    const [flows, setFlows] = useState([]);
    const [currentFlow, setCurrentFlow] = useState('');

    const handleAddFlow = () => {
        if (currentFlow) {
            setFlows([...flows, currentFlow]);
            setCurrentFlow('');
        }
    };

    const handleDeleteFlow = (index) => {
        const newFlows = flows.filter((_, i) => i !== index);
        setFlows(newFlows);
    };

    return (
        <div className="flow-builder">
            <h2 className="text-lg font-bold">Flow Builder</h2>
            <input
                type="text"
                value={currentFlow}
                onChange={(e) => setCurrentFlow(e.target.value)}
                placeholder="Enter flow name"
                className="border p-2 rounded"
            />
            <button onClick={handleAddFlow} className="bg-blue-500 text-white p-2 rounded">
                Add Flow
            </button>
            <ul className="mt-4">
                {flows.map((flow, index) => (
                    <li key={index} className="flex justify-between items-center">
                        <span>{flow}</span>
                        <button onClick={() => handleDeleteFlow(index)} className="text-red-500">
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FlowBuilder;
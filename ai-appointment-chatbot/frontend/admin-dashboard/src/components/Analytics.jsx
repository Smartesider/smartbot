import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Analytics = () => {
    const [analyticsData, setAnalyticsData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAnalyticsData = async () => {
            try {
                const response = await axios.get('/api/analytics'); // Adjust the endpoint as necessary
                setAnalyticsData(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchAnalyticsData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error fetching analytics data: {error.message}</div>;
    }

    return (
        <div className="analytics">
            <h2>Analytics Overview</h2>
            <div>
                <h3>Top 10 Questions</h3>
                <ul>
                    {analyticsData.topQuestions.map((question, index) => (
                        <li key={index}>{question}</li>
                    ))}
                </ul>
            </div>
            <div>
                <h3>Booking Rate</h3>
                <p>{analyticsData.bookingRate}%</p>
            </div>
            <div>
                <h3>Error Messages</h3>
                <ul>
                    {analyticsData.errorMessages.map((errorMsg, index) => (
                        <li key={index}>{errorMsg}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Analytics;
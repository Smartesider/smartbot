import React, { useState } from 'react';

const Settings = () => {
    const [settings, setSettings] = useState({
        notificationEnabled: true,
        emailNotifications: true,
        smsNotifications: false,
    });

    const handleChange = (e) => {
        const { name, checked } = e.target;
        setSettings((prevSettings) => ({
            ...prevSettings,
            [name]: checked,
        }));
    };

    const handleSave = () => {
        // Logic to save settings to the backend
        console.log('Settings saved:', settings);
    };

    return (
        <div className="settings-container">
            <h2 className="text-lg font-bold">Settings</h2>
            <div className="settings-option">
                <label>
                    <input
                        type="checkbox"
                        name="notificationEnabled"
                        checked={settings.notificationEnabled}
                        onChange={handleChange}
                    />
                    Enable Notifications
                </label>
            </div>
            <div className="settings-option">
                <label>
                    <input
                        type="checkbox"
                        name="emailNotifications"
                        checked={settings.emailNotifications}
                        onChange={handleChange}
                    />
                    Email Notifications
                </label>
            </div>
            <div className="settings-option">
                <label>
                    <input
                        type="checkbox"
                        name="smsNotifications"
                        checked={settings.smsNotifications}
                        onChange={handleChange}
                    />
                    SMS Notifications
                </label>
            </div>
            <button onClick={handleSave} className="mt-4 bg-blue-500 text-white p-2 rounded">
                Save Settings
            </button>
        </div>
    );
};

export default Settings;
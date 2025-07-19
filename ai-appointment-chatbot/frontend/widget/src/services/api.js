import axios from 'axios';
import { API_BASE_URL } from '../../shared/constants/api_endpoints';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Function to create an appointment
export const createAppointment = async (appointmentData) => {
    try {
        const response = await apiClient.post('/appointments', appointmentData);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error.message;
    }
};

// Function to update an appointment
export const updateAppointment = async (appointmentId, appointmentData) => {
    try {
        const response = await apiClient.put(`/appointments/${appointmentId}`, appointmentData);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error.message;
    }
};

// Function to delete an appointment
export const deleteAppointment = async (appointmentId) => {
    try {
        const response = await apiClient.delete(`/appointments/${appointmentId}`);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error.message;
    }
};

// Function to fetch available time slots
export const fetchAvailableTimeSlots = async (date) => {
    try {
        const response = await apiClient.get(`/appointments/available?date=${date}`);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error.message;
    }
};

// Function to send a message in chat
export const sendMessage = async (messageData) => {
    try {
        const response = await apiClient.post('/chat/messages', messageData);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error.message;
    }
};
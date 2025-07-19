import axios from 'axios';
import { API_BASE_URL } from '../../../shared/constants/api_endpoints';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Example function to login
export const login = async (credentials) => {
  try {
    const response = await apiClient.post('/auth/login', credentials);
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error.message;
  }
};

// Example function to fetch appointments
export const fetchAppointments = async () => {
  try {
    const response = await apiClient.get('/appointments');
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error.message;
  }
};

// Example function to create an appointment
export const createAppointment = async (appointmentData) => {
  try {
    const response = await apiClient.post('/appointments', appointmentData);
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error.message;
  }
};

// Example function to fetch analytics data
export const fetchAnalytics = async () => {
  try {
    const response = await apiClient.get('/analytics');
    return response.data;
  } catch (error) {
    throw error.response ? error.response.data : error.message;
  }
};
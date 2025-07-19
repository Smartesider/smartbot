const API_BASE_URL = 'https://api.example.com'; // Replace with your actual API base URL

export const AUTH_ENDPOINTS = {
    LOGIN: `${API_BASE_URL}/auth/login`,
    REGISTER: `${API_BASE_URL}/auth/register`,
};

export const APPOINTMENT_ENDPOINTS = {
    CREATE: `${API_BASE_URL}/appointments/create`,
    UPDATE: `${API_BASE_URL}/appointments/update`,
    DELETE: `${API_BASE_URL}/appointments/delete`,
    GET_ALL: `${API_BASE_URL}/appointments`,
};

export const CHAT_ENDPOINTS = {
    SEND_MESSAGE: `${API_BASE_URL}/chat/send`,
    GET_MESSAGES: `${API_BASE_URL}/chat/messages`,
};

export const WEBHOOK_ENDPOINTS = {
    GOOGLE_CALENDAR: `${API_BASE_URL}/webhooks/google-calendar`,
};
# AI Appointment Chatbot

## Overview
The AI Appointment Chatbot is a web application designed to facilitate appointment management and chat interactions using AI. It integrates with Google Calendar for scheduling and provides real-time notifications via email and SMS.

## Features
1. **Appointment Management**: Create, update, and delete appointments directly through the chat interface.
2. **Chat Functionality**: Engage in conversations with the chatbot, which utilizes AI for understanding and responding to user queries.
3. **Notifications**: Receive reminders and notifications via email and SMS for upcoming appointments.
4. **User Authentication**: Secure login and registration for users.
5. **Real-time Availability Check**: Check available time slots using Google Calendar API.

## Technologies Used
- **Backend**: Python (FastAPI)
- **Frontend**: React
- **Database**: PostgreSQL
- **Caching**: Redis
- **AI Engine**: OpenAI GPT-4o
- **Notifications**: Twilio (SMS), Sendgrid (Email)
- **Deployment**: Docker

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-appointment-chatbot.git
   cd ai-appointment-chatbot
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Configure environment variables by copying `.env.example` to `.env` and updating the values.

3. Set up the frontend:
   - Navigate to the `frontend/widget` directory.
   - Install dependencies:
     ```
     npm install
     ```

4. Run the application:
   - Start the backend server:
     ```
     uvicorn src.main:app --reload
     ```
   - Start the frontend:
     ```
     npm start
     ```

## Usage
- Access the chatbot through the widget integrated into your web application.
- Use the chat interface to manage appointments and interact with the AI.
- Notifications will be sent via email and SMS based on your preferences.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
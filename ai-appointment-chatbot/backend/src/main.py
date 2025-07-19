from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth.routes import router as auth_router
from api.appointments.routes import router as appointment_router
from api.chat.routes import router as chat_router
from api.webhooks.routes import router as webhook_router
from core.config import settings

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(appointment_router, prefix="/appointments", tags=["appointments"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(webhook_router, prefix="/webhooks", tags=["webhooks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Appointment Chatbot API"}
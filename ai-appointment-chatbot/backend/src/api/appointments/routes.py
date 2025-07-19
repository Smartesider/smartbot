from fastapi import APIRouter, HTTPException
from typing import List
from ..models.appointment import Appointment
from ..services.calendar_service import CalendarService

router = APIRouter()
calendar_service = CalendarService()

@router.post("/appointments/", response_model=Appointment)
async def create_appointment(appointment: Appointment):
    try:
        created_appointment = await calendar_service.create_event(appointment)
        return created_appointment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/appointments/{appointment_id}", response_model=Appointment)
async def update_appointment(appointment_id: str, appointment: Appointment):
    try:
        updated_appointment = await calendar_service.update_event(appointment_id, appointment)
        return updated_appointment
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/appointments/{appointment_id}", response_model=dict)
async def delete_appointment(appointment_id: str):
    try:
        await calendar_service.delete_event(appointment_id)
        return {"detail": "Appointment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/appointments/", response_model=List[Appointment])
async def get_appointments():
    try:
        appointments = await calendar_service.get_all_events()
        return appointments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
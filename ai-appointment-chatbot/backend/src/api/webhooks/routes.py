from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class WebhookRequest(BaseModel):
    event_type: str
    data: dict

@router.post("/webhook")
async def handle_webhook(request: WebhookRequest):
    try:
        # Process the incoming webhook event
        event_type = request.event_type
        data = request.data
        
        # Add your logic to handle different event types here
        if event_type == "appointment.created":
            # Handle appointment creation
            pass
        elif event_type == "appointment.updated":
            # Handle appointment update
            pass
        elif event_type == "appointment.canceled":
            # Handle appointment cancellation
            pass
        else:
            raise HTTPException(status_code=400, detail="Unknown event type")

        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
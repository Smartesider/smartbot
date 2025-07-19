from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Message(BaseModel):
    user_id: str
    content: str

class Conversation(BaseModel):
    user_id: str
    messages: List[Message]

@router.post("/conversations", response_model=Conversation)
async def create_conversation(conversation: Conversation):
    # Logic to create a new conversation
    return conversation

@router.get("/conversations/{user_id}", response_model=List[Message])
async def get_conversation(user_id: str):
    # Logic to retrieve conversation for a specific user
    return []

@router.delete("/conversations/{user_id}")
async def delete_conversation(user_id: str):
    # Logic to delete a conversation for a specific user
    return {"message": "Conversation deleted successfully"}
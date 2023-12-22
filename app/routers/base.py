from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.users import User as UserModel
from app.schemas.base import EmailRequest

router = APIRouter()


@router.post("/ses-mail", response_model=None)
async def send_ses_emails(req: EmailRequest):
    return req

from fastapi import APIRouter, Form
from pydantic import EmailStr, BaseModel
from app.utils.send_mail import send_mail


mail_router = APIRouter()

@mail_router.post("/", summary="Contact Mail")
async def contact_mail(firstName: str = Form(),lastName: str = Form(),email: str = Form(),subject: str = Form(),message: str = Form(),):
    send_mail(
        firstName = firstName,
        lastName = lastName,
        email = email,
        subject = subject,
        message = message
    )
    return {"message": "Contact Mail Sent"}
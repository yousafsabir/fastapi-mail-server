from fastapi import APIRouter
from app.routes.mail_routes import mail_router

router = APIRouter()

router.include_router(mail_router, prefix="/mail", tags=["Mail"])

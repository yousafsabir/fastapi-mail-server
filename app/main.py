from fastapi import FastAPI, Request, Response, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from app.config.config import settings
from app.routes.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Nothing here bro"}


app.include_router(router, prefix=settings.API)

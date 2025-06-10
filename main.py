from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="Profitable Business Discovery Tool")

app.include_router(api_router)

from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI(title="Profitable Business Discovery Tool")

app.include_router(api_router)

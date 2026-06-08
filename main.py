from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="LifeOS - AI Second Brain")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "LifeOS backend is running "}

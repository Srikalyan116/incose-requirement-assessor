from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Requirements Compliance Service")
app.include_router(router)

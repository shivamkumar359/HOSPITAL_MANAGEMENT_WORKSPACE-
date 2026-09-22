from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Hospital Management Chatbot API",
    description="Phase 1 backend foundation for the Hospital Management Chatbot",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Hospital Management Chatbot API is running"}
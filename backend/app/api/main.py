from fastapi import FastAPI, status
from app.api.endpoints import health_check
from config.settings import settings

app = FastAPI()

# Include routers
app.include_router(health_check.router, tags=["healthcheck"])

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": settings.SPECIAL_MESSAGE}


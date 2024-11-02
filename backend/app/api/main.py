import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import health_check
from config.settings import settings
from app.logging.log_config import log_config

log_config.configure_logging()
logger = log_config.get_logger()

logger.info("Starting FastAPI server...")

app = FastAPI(description="FastAPI Base Project")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_check.router, tags=["healthcheck"])

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    logger.debug("debug level: Root endpoint accessed.")
    logger.info("info level: Root endpoint accessed.")
    logger.warning("warning level: Root endpoint accessed.")
    logger.error("error level: Root endpoint accessed.")
    return {"message": settings.SPECIAL_MESSAGE}

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
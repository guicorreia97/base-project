# app/core/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

# Load the main .env file to get the APP_ENV variable for local development
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError("Main .env file not found")

# Determine the environment-specific .env file
app_env = os.getenv('APP_ENV', 'development')
env_file_path = f"config/envs/.env.{app_env}"

# Check if the environment-specific .env file exists
if not os.path.exists(env_file_path):
    raise FileNotFoundError(f".env file for {app_env} environment not found. Create a .env.{app_env} file in the envs folder.")

class Settings(BaseSettings):
    APP_ENV: str = app_env
    
    class Config:
        # Reference the dynamically set env file path
        env_file = env_file_path
        env_file_encoding = 'utf-8'

    # Define your settings here (they will be read from environment variables if available)
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    SPECIAL_MESSAGE: str = "Hello."

# Instantiate the Settings object, loading environment variables
settings = Settings()

if __name__ == "__main__":
    print(settings.APP_ENV)
    print(settings.SPECIAL_MESSAGE)

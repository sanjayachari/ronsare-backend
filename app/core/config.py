# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Use a `.env` file in development or set environment variables in production.
    """

    # FastAPI app configuration
    APP_NAME: str = "FastAPI Example App"  # Name of the application
    APP_VERSION: str = "1.0.0"            # Version of the application
    DEBUG: bool = True                     # Toggle debug mode

    # Database configuration
    DB_USER: str = "postgres"              # Database username
    DB_PASSWORD: str = "password"          # Database password
    DB_HOST: str = "localhost"             # Database host
    DB_PORT: int = 5432                    # Database port
    DB_NAME: str = "mydatabase"            # Database name

    # Security / Authentication
    SECRET_KEY: str = "supersecretkey"     # Used for JWT or password hashing
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # JWT token expiration in minutes

    # Other optional settings
    LOG_LEVEL: str = "info"                # Logging level

    class Config:
        env_file = ".env"                  # Load environment variables from `.env` file
        env_file_encoding = "utf-8"

# Create a single settings instance to import anywhere in the project
settings = Settings()

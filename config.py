import os  # Provides functions for interacting with the operating system, including accessing environment variables
from pathlib import Path  # Offers classes to handle file system paths in a more object-oriented and readable way
from dotenv import load_dotenv  # Loads environment variables from a .env file into the system's environment variables
from urllib.parse import quote_plus  # Encodes special characters in strings, particularly useful for constructing URLs
from pydantic_settings import BaseSettings  # Provides a way to manage application settings using Pydantic, enabling data validation and settings management

# Define the path to the .env file
env_path = Path(".") / ".env"

# Load environment variables from the .env file
load_dotenv(dotenv_path=env_path)

# Define a Pydantic settings class to manage configuration
class Settings(BaseSettings):
    
    # Fetching the database user from environment variables
    DB_USER: str = os.getenv("DB_USER")
    
    # Fetching the database host from environment variables
    DB_HOST: str = os.getenv("DB_HOST")
    
    # Fetching the database name from environment variables
    DB_NAME: str = os.getenv("DB_NAME")
    
    # Fetching the database password from environment variables
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    
    # Fetching the database port from environment variables
    DB_PORT: str = os.getenv("DB_PORT")
    
    # Constructing the complete database URL using the fetched environment variables
    DATABASE_URL: str = f'postgresql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

def get_settings() -> Settings:
    return Settings()
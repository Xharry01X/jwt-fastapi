from sqlalchemy import create_engine  # Imports the create_engine function to establish a connection to the database
from sqlalchemy.orm import sessionmaker, declarative_base  # Imports sessionmaker to create a session factory, and declarative_base to create a base class for declarative class definitions
from typing import Generator  # Imports Generator type hint for the get_db function
from config import get_settings  # Imports the get_settings function from the config module to fetch the application settings

# Fetch the settings which include the database URL
settings = get_settings()

# Create an SQLAlchemy engine with the database URL and additional parameters for connection pooling
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Checks the connection before using it from the pool
    pool_recycle=300,  # Recycles connections after 300 seconds
    pool_size=5,  # Maintains a pool of 5 connections
    max_overflow=0  # Disables overflow connections
)

# Create a configured "Session" class bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Dependency to get a database session for each request, ensuring proper closing of the session
def get_db() -> Generator:
    db = SessionLocal()  # Creates a new session
    try:
        yield db  # Provides the session to the caller
    finally:
        db.close()  # Closes the session after the request is complete

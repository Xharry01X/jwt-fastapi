from sqlalchemy import create_engine
from database import Base
from models import UserModel  # Import your User model
from config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

from sqlalchemy import Boolean, Column, Integer, String, DateTime, func  # Importing necessary SQLAlchemy components
from database import Base  # Importing the Base class from database.py

# Define the User model
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(100))

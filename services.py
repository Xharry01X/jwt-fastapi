from models import UserModel  # Importing the UserModel class
from fastapi.exceptions import HTTPException  # Importing HTTPException for error handling
from security import get_password_hash  # Importing the password hashing function
from sqlalchemy.orm import Session  # Importing Session for type hinting

async def create_user_account(data, db: Session):
    # Check if the user already exists
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered")
    
    # Create a new user instance
    new_user = UserModel(
        email=data.email,
        password=get_password_hash(data.password)
    )
    
    # Add and commit the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

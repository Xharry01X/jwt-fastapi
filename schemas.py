from pydantic import BaseModel, EmailStr  # Importing BaseModel and EmailStr for data validation

# Define a Pydantic model for user creation request
class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str

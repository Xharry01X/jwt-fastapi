from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from database import get_db
from schemas import CreateUserRequest
from services import create_user_account

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)
    payload = {"Message": "User created"}
    return JSONResponse(content=payload)

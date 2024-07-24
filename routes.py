from fastapi import APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users"
    tags=["User"]
    responses={404:{"description":"Not found"}}
)
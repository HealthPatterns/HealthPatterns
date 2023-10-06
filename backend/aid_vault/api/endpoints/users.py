from fastapi import APIRouter, HTTPException, status, Response

from ...db.database import SessionInstance

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("")
def get_users():
    return

@router.post("")
def create_user():
    return

@router.put("/{uuid}")
def put_user():
    return

@router.delete("/{uuid}")
def delete_user():
    return

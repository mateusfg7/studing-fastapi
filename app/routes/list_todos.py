from fastapi import APIRouter
from typing import Union

from services import todo_service

router = APIRouter()


@router.get('/list')
def list_todos(completed: Union[bool, None] = None):
    return todo_service.list_all(completed)

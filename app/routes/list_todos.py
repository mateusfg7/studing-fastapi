from fastapi import APIRouter
from typing import Union

from app.database import Todo, todos

router = APIRouter()


def filter_todos(todo: Todo, completed: bool):
    return todo['completed'] == completed


@router.get('/list')
def list_todos(completed: Union[bool, None] = None):
    if completed == None:
        return todos
    else:
        return list(filter(
            lambda todo: filter_todos(todo, completed),
            todos
        ))

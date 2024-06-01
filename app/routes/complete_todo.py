from fastapi import APIRouter

from models.db import Todo
from database import todos

router = APIRouter()


@router.put('/toggle-completed/{todo_id}')
def complete_todo(todo_id: int):
    global todos

    updated_todos: list[Todo] = []
    completed = None
    for todo in todos:
        if todo['id'] == todo_id:
            updated_todos.append({**todo, 'completed': not todo['completed']})
            completed = not todo['completed']
        else:
            updated_todos.append(todo)

    todos = updated_todos.copy()
    return {'message': f'Todo {todo_id} marked as {'Completed' if completed else 'Uncompleted'}'}

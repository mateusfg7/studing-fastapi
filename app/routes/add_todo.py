from fastapi import APIRouter

from datetime import datetime
from pydantic import BaseModel

from app.database import Todo, todos

router = APIRouter()


def id_is_duplicated(todos: list[Todo], id: int):
    if any(todo['id'] == id for todo in todos):
        return True
    else:
        return False


class NewTodo(BaseModel):
    id: int
    title: str


@router.post('/add')
def create_todo(new_todo: NewTodo):
    if id_is_duplicated(todos, new_todo.id):
        return {'error': f'There is already a todo with ID = {new_todo.id}'}
    else:
        todo: Todo = {
            'id': new_todo.id,
            'title': new_todo.title,
            'completed': False,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        todos.append(todo)
        return {'message': 'Todo created successfully!', 'todo': todo}

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from app.database import todos, Todo

app = FastAPI()

def filter_todos(todo: Todo, completed: bool):
    return todo['completed'] == completed

@app.get('/list')
def list_todos(completed: Union[bool, None] = None):
    if completed == None:
        return todos
    else:
        return list(filter(
            lambda todo: filter_todos(todo, completed),
            todos
        ))

def id_is_duplicated(todos: list[Todo], id: int):
    if any(todo['id'] == id for todo in todos):
        return True
    else:
        return False

class NewTodo(BaseModel):
    id: int
    title: str
    
@app.post('/add')
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
    
@app.put('/toggle-completed/{todo_id}')
def complete_todo(todo_id: int):
    global todos
    
    updated_todos: list[Todo] = []
    completed = None
    for todo in todos:
        if todo['id'] == todo_id:
            updated_todos.append({ **todo, 'completed': not todo['completed'] })
            completed = not todo['completed']
        else:
            updated_todos.append(todo)
    
    todos = updated_todos.copy()
    return {'message': f'Todo {todo_id} marked as {'Completed' if completed else 'Uncompleted'}'}
        
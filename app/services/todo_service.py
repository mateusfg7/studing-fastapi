from datetime import datetime
from typing import Union

from models.db import Todo
from database import todos


def add(id: int, title: str) -> Todo:
    todo: Todo = {
        'id': id,
        'title': title,
        'completed': False,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    todos.append(todo)

    return todo


def get_by_id(id: int) -> Todo | None:
    founded_todos: list[Todo] = []

    for todo in todos:
        if todo['id'] == id:
            founded_todos.append(todo)

    if len(founded_todos) == 0:
        return None
    else:
        return founded_todos[0]


def toggle_completed(todo_id: int):
    global todos

    updated_todos: list[Todo] = []
    completed = None
    for todo in todos:
        if todo['id'] == todo_id:
            updated_todos.append(
                {**todo, 'completed': not todo['completed'], 'updated_at': datetime.now()})
            completed = not todo['completed']
        else:
            updated_todos.append(todo)

    todos = updated_todos.copy()
    return completed


def filter_todos(todo: Todo, completed: bool):
    return todo['completed'] == completed


def list_all(completed: Union[bool, None] = None) -> list[Todo]:
    if completed == None:
        return todos
    else:
        return list(filter(
            lambda todo: filter_todos(todo, completed),
            todos
        ))

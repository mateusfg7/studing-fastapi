from datetime import datetime

from database import todos

from models.db import Todo


def add(id: int, title: str, completed: bool) -> Todo:
    todo = Todo(id=id, completed=completed, title=title,
                created_at=datetime.now(), updated_at=datetime.now())

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

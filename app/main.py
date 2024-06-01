from fastapi import FastAPI

from app.routes import list_todos
from app.routes import add_todo
from app.routes import complete_todo

app = FastAPI()

app.include_router(list_todos.router)
app.include_router(add_todo.router)
app.include_router(complete_todo.router)

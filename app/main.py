from fastapi import FastAPI

from routes import list_todos
from routes import add_todo
from routes import complete_todo

app = FastAPI()

app.include_router(list_todos.router)
app.include_router(add_todo.router)
app.include_router(complete_todo.router)

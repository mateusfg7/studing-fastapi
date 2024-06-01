from pydantic import BaseModel

class NewTodo(BaseModel):
    id: int
    title: str
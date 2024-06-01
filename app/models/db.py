from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime

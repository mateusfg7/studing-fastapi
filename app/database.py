"""
WARNING
Por enquanto esse é apenas um exemplo de um banco de dados salvo na memória, através de uma veriável.

Mais pra frente será substituido por um SGBD, provavelmente PostegreSQL.
"""

from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime

todos: list[Todo] = [
    {
        'id': 0,
        'title': 'Estudar FastAPI',
        'completed': False,
        'created_at': datetime.now(),
        'update_at': datetime.now()
    },
    {
        'id': 1,
        'title': 'Iniciar Trading Bot',
        'completed': True,
        'created_at': datetime.now(),
        'update_at': datetime.now()
    },
    {
        'id': 2,
        'title': 'Configurar Docker',
        'completed': False,
        'created_at': datetime.now(),
        'update_at': datetime.now()
    },
]
    
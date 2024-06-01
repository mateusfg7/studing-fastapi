"""
WARNING
Por enquanto esse é apenas um exemplo de um banco de dados salvo na memória, através de uma veriável.

Mais pra frente será substituido por um SGBD, provavelmente PostegreSQL.
"""

from datetime import datetime

from models.db import Todo


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

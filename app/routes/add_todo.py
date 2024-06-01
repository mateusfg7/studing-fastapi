from fastapi import APIRouter

from models.dto import NewTodo

from services import todo_service


router = APIRouter()


@router.post('/add')
def add_todo(new_todo: NewTodo):
    if todo_service.get_by_id(new_todo.id) != None:
        return {'error': f'There is already a todo with ID = {new_todo.id}'}
    else:
        todo = todo_service.add(id=new_todo.id, title=new_todo.title)
        return {'message': 'Todo created successfully!', 'todo': todo}

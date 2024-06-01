from fastapi import APIRouter

from services import todo_service

router = APIRouter()


@router.put('/toggle-completed/{todo_id}')
def complete_todo(todo_id: int):
    if not todo_service.get_by_id(todo_id):
        return {
            'message': 'Todo not found!'
        }

    completed = todo_service.toggle_completed(todo_id)
    return {
        'message': f'Todo {todo_id} marked as {'Completed' if completed else 'Uncompleted'}'
    }

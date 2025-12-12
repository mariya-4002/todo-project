from .models import Todo

def create_in_db(data):
    todo = Todo.objects.create(
        title=data.title,
        description=data.description
    )
    return {"id": todo.id, "message": "Todo created"}

def update_in_db(todo_id, data):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.title = data.title
        todo.description = data.description
        todo.save()
        return {"message": "Todo updated"}
    except Todo.DoesNotExist:
        return {"error": "Todo not found"}

def get_from_db(todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        return {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
    except Todo.DoesNotExist:
        return {"error": "Todo not found"}

def get_all_from_db():
    return list(Todo.objects.all().values())

def delete_from_db(todo_id):
    try:
        Todo.objects.get(id=todo_id).delete()
        return {"message": "Todo deleted"}
    except Todo.DoesNotExist:
        return {"error": "Todo not found"}

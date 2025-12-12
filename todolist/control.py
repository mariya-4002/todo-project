from .models import Todo

def create_todo(title, description):
    todo = Todo.objects.create(title=title, description=description)
    return todo

def fetch_all_todos():
    return Todo.objects.all()

def fetch_one_todo(id):
    return Todo.objects.get(id=id)

def update_todo_item(id, title, description):
    todo = Todo.objects.get(id=id)
    todo.title = title
    todo.description = description
    todo.save()
    return todo

def delete_todo_item(id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return True

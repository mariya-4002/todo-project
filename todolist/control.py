from .models import Todo

# GET all todos
def get_all():
    return Todo.objects.all()

# GET one todo
def get_one(todo_id):
    return Todo.objects.get(id=todo_id)

# CREATE
def create(title, description):
    return Todo.objects.create(title=title, description=description)

# UPDATE
def update(todo_id, title, description):
    todo = Todo.objects.get(id=todo_id)
    todo.title = title
    todo.description = description
    todo.save()
    return todo

# DELETE
def delete(todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return True

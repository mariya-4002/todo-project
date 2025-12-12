from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def _str_(self):
        return self.title

    # -------------------------
    # CREATE – Save data
    # -------------------------
    @staticmethod
    def create_todo(data):
        todo = Todo.objects.create(
            title=data.title,
            description=data.description
        )
        return todo

    # -------------------------
    # UPDATE – Update existing
    # -------------------------
    @staticmethod
    def update_todo(todo_id, data):
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.title = data.title
            todo.description = data.description
            todo.save()
            return todo
        except Todo.DoesNotExist:
            return None

    # -------------------------
    # GET SINGLE – Fetch one
    # -------------------------
    @staticmethod
    def get_todo(todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None

    # -------------------------
    # GET ALL – Fetch all todos
    # -------------------------
    @staticmethod
    def get_all_todos():
        return Todo.objects.all()

    # -------------------------
    # DELETE – Remove a todo
    # -------------------------
    @staticmethod
    def delete_todo(todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return True
        except Todo.DoesNotExist:
            return False

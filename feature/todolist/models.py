from django.db import models
from django.core.exceptions import ObjectDoesNotExist



class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    # ---------------- CREATE ----------------
    @classmethod
    def create_todo(cls, data: dict):
        try:
            todo = cls.objects.create(
                title=data["title"],
                description=data["description"]
            )
            return success_response(
                message="Todo created successfully",
                data={
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description
                },
                status_code=201
            )
        except Exception as e:
            return error_response(
                message="Failed to create todo",
                errors=str(e)
            )

    # ---------------- UPDATE ----------------
    @classmethod
    def update_todo(cls, todo_id: int, data: dict):
        try:
            todo = cls.objects.get(id=todo_id)
            todo.title = data["title"]
            todo.description = data["description"]
            todo.save()

            return success_response(
                message="Todo updated successfully",
                data={
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description
                }
            )
        except ObjectDoesNotExist:
            return error_response(
                message="Todo not found",
                status_code=404
            )
        except Exception as e:
            return error_response(
                message="Failed to update todo",
                errors=str(e)
            )

    # ---------------- GET ONE ----------------
    @classmethod
    def get_todo(cls, todo_id: int):
        try:
            todo = cls.objects.get(id=todo_id)
            return success_response(
                message="Todo fetched successfully",
                data={
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description
                }
            )
        except ObjectDoesNotExist:
            return error_response(
                message="Todo not found",
                status_code=404
            )

    # ---------------- GET ALL ----------------
    @classmethod
    def get_all_todos(cls):
        try:
            todos = cls.objects.all().order_by("-id")
            data = [
                {
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description
                }
                for todo in todos
            ]

            return success_response(
                message="Todos fetched successfully",
                data=data
            )
        except Exception as e:
            return error_response(
                message="Failed to fetch todos",
                errors=str(e)
            )

    # ---------------- DELETE ----------------
    @classmethod
    def delete_todo(cls, todo_id: int):
        try:
            todo = cls.objects.get(id=todo_id)
            todo.delete()

            return success_response(
                message="Todo deleted successfully"
            )
        except ObjectDoesNotExist:
            return error_response(
                message="Todo not found",
                status_code=404
            )

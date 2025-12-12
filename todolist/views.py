from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import control
from .models import Todo


@api_view(['POST'])
def create_todo(request):
    todo_data = control.parse_create_request(request.data)
    todo = Todo.objects.create(
        title=todo_data.title,
        description=todo_data.description
    )
    return Response({"message": "Todo created", "id": todo.id})


@api_view(['GET'])
def get_all_todos(request):
    todos = Todo.objects.all().values()
    return Response(list(todos))


@api_view(['GET'])
def get_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        return Response({"id": todo.id, "title": todo.title, "description": todo.description})
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    todo_data = control.parse_update_request(request.data)

    todo.title = todo_data.title
    todo.description = todo_data.description
    todo.save()

    return Response({"message": "Todo updated"})


@api_view(['DELETE'])
def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return Response({"message": "Todo deleted"})
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

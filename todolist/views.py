from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .control import (
    create_todo,
    fetch_all_todos,
    fetch_one_todo,
    update_todo_item,
    delete_todo_item
)

from .serializers import (
    TodoCreateRequestSerializer,
    TodoUpdateRequestSerializer,
    TodoResponseSerializer,
)

from .dataclass import TodoDataClass


def convert_to_dataclass(todo_obj):
    return TodoDataClass(
        id=todo_obj.id,
        title=todo_obj.title,
        description=todo_obj.description,
        created_at=str(todo_obj.created_at)
    )


@api_view(["POST"])
def add_todo(request):
    serializer = TodoCreateRequestSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.validated_data

        todo = create_todo(data["title"], data["description"])

        dc = convert_to_dataclass(todo)
        response = TodoResponseSerializer(dc.__dict__)

        return Response(response.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_all_todos(request):
    todos = fetch_all_todos()
    result = [TodoResponseSerializer(convert_to_dataclass(t).__dict__).data for t in todos]
    return Response(result)



@api_view(["GET"])
def get_todo(request, id):
    todo = fetch_one_todo(id)
    dc = convert_to_dataclass(todo)
    return Response(TodoResponseSerializer(dc.__dict__).data)



@api_view(["PUT"])
def update_todo(request, id):
    serializer = TodoUpdateRequestSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.validated_data

        todo = update_todo_item(id, data["title"], data["description"])

        dc = convert_to_dataclass(todo)
        return Response(TodoResponseSerializer(dc.__dict__).data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def delete_todo(request, id):
    delete_todo_item(id)
    return Response({"message": "Todo deleted successfully"})

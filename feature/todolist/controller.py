from rest_framework.decorators import api_view

from .models import Todo
from .util.response import success_response, error_response, paginate_queryset

from .serializers.request.create_todo import CreateTodoRequestSerializer
from .serializers.request.update_todo import UpdateTodoRequestSerializer
from .serializers.request.get_todo import GetTodoRequestSerializer
from .serializers.request.get_all_todo import GetAllTodoRequestSerializer
from .serializers.request.delete_todo import DeleteTodoRequestSerializer

@api_view(['POST'])
def create_api(request):
    serializer = CreateTodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    todo = Todo.create_todo(serializer.validated_data)

    return success_response(
        message="Todo created successfully",
        data={
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        },
        status_code=201
    )

@api_view(['PUT'])
def update_api(request):
    serializer = UpdateTodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = serializer.validated_data

    try:
        todo = Todo.update_todo(data["id"], data)
    except Todo.DoesNotExist:
        return error_response("Todo not found", status_code=404)

    return success_response(
        message="Todo updated successfully",
        data={
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
    )

@api_view(['GET'])
def get_api(request):
    serializer = GetTodoRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    try:
        todo = Todo.get_todo(serializer.validated_data["id"])
    except Todo.DoesNotExist:
        return error_response("Todo not found", status_code=404)

    return success_response(
        message="Todo fetched successfully",
        data={
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
    )

@api_view(['GET'])
def get_all_api(request):
    serializer = GetAllTodoRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    page = serializer.validated_data.get("page", 1)
    limit = serializer.validated_data.get("limit", 10)

    queryset = Todo.get_all_todos()
    paginated = paginate_queryset(queryset, page, limit)

    paginated["results"] = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
        for todo in paginated["results"]
    ]

    return success_response(
        message="Todos fetched successfully",
        data=paginated
    )

@api_view(['DELETE'])
def delete_api(request):
    serializer = DeleteTodoRequestSerializer(
        data=request.query_params or request.data
    )

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    try:
        Todo.delete_todo(serializer.validated_data["id"])
    except Todo.DoesNotExist:
        return error_response("Todo not found", status_code=404)

    return success_response("Todo deleted successfully")

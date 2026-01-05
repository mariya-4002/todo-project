from rest_framework.decorators import api_view
from .models import Todo

from feature.common.response import success_response, error_400, error_404
from feature.common.pagination import paginate_queryset



from .serializers.request.create_todo import CreateTodoRequestSerializer
from .serializers.request.update_todo import UpdateTodoRequestSerializer
from .serializers.request.get_todo import GetTodoRequestSerializer
from .serializers.request.get_all_todo import GetAllTodoRequestSerializer
from .serializers.request.delete_todo import DeleteTodoRequestSerializer



@api_view(['POST'])
def create_todo(request):
    serializer = CreateTodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_400(serializer.errors)

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
def update_todo(request):
    serializer = UpdateTodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    todo = Todo.update_todo(
        serializer.validated_data["id"],
        serializer.validated_data
    )

    if not todo:
        return error_404()

    return success_response(
        message="Todo updated successfully",
        data={
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
    )


@api_view(['GET'])
def get_todo(request):
    serializer = GetTodoRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    todo = Todo.get_todo(serializer.validated_data["id"])

    if not todo:
        return error_404()

    return success_response(
        data={
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
    )


@api_view(['GET'])
def get_all_todo(request):
    serializer = GetAllTodoRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    page = serializer.validated_data.get("page", 1)
    limit = serializer.validated_data.get("limit", 10)

    paginated = paginate_queryset(
        Todo.get_all_todos(),
        page,
        limit
    )

    paginated["results"] = [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description
        }
        for t in paginated["results"]
    ]

    return success_response(data=paginated)



@api_view(['DELETE'])
def delete_todo(request):
    serializer = DeleteTodoRequestSerializer(
        data=request.query_params or request.data
    )

    if not serializer.is_valid():
        return error_400(serializer.errors)

    deleted = Todo.delete_todo(serializer.validated_data["id"])

    if not deleted:
        return error_404()

    return success_response(message="Todo deleted successfully")

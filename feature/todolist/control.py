from rest_framework.decorators import api_view

from .serializers import TodoSerializer
from .models import Todo
from .views import (
    create_in_db,
    update_in_db,
    get_from_db,
    delete_from_db
)

from .util.response import (
    success_response,
    error_response,
    paginate_queryset,
    parse_int
)


# -------------------- CREATE --------------------
@api_view(['POST'])
def create_api(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        data_obj = serializer.create()
        result = create_in_db(data_obj)

        return success_response(
            message="Todo created successfully",
            data=result,
            status_code=201
        )

    return error_response(
        message="Validation failed",
        errors=serializer.errors,
        status_code=400
    )


# -------------------- UPDATE --------------------
@api_view(['PUT'])
def update_api(request):
    todo_id = request.data.get("id")

    if not todo_id:
        return error_response(
            message="id is required",
            status_code=400
        )

    try:
        instance = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return error_response(
            message="Todo not found",
            status_code=404
        )

    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        data_obj = serializer.update(instance)
        result = update_in_db(todo_id, data_obj)

        return success_response(
            message="Todo updated successfully",
            data=result
        )

    return error_response(
        message="Validation failed",
        errors=serializer.errors,
        status_code=400
    )


# -------------------- GET ONE --------------------
@api_view(['GET'])
def get_api(request):
    todo_id = request.query_params.get("id")

    if not todo_id:
        return error_response(
            message="id is required",
            status_code=400
        )

    result = get_from_db(todo_id)

    if "error" in result:
        return error_response(
            message=result["error"],
            status_code=404
        )

    return success_response(
        message="Todo fetched successfully",
        data=result
    )


# -------------------- GET ALL (WITH PAGINATION) --------------------
@api_view(['GET'])
def get_all_api(request):
    page = parse_int(request.query_params.get("page"), 1)
    limit = parse_int(request.query_params.get("limit"), 5)

    queryset = Todo.objects.all().order_by("-id")

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


# -------------------- DELETE --------------------
@api_view(['DELETE'])
def delete_api(request):
    todo_id = request.data.get("id")

    if not todo_id:
        return error_response(
            message="id is required",
            status_code=400
        )

    result = delete_from_db(todo_id)

    if "error" in result:
        return error_response(
            message=result["error"],
            status_code=404
        )

    return success_response(
        message="Todo deleted successfully"
    )

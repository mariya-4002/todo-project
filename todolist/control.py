from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .views import (
    create_in_db, update_in_db, get_from_db,
    get_all_from_db, delete_from_db
)
from .models import Todo


# CREATE API
@api_view(['POST'])
def create_api(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        data_obj = serializer.create()   # dataclass created here
        result = create_in_db(data_obj)
        return Response(result)

    return Response(serializer.errors, status=400)


# UPDATE API
@api_view(['PUT'])
def update_api(request, id):
    try:
        instance = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=404)

    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        data_obj = serializer.update(instance)  # dataclass updated
        result = update_in_db(id, data_obj)
        return Response(result)

    return Response(serializer.errors, status=400)


# GET ONE API
@api_view(['GET'])
def get_api(request, id):
    result = get_from_db(id)
    return Response(result)


# GET ALL API
@api_view(['GET'])
def get_all_api(request):
    result = get_all_from_db()
    return Response(result)


# DELETE API
@api_view(['DELETE'])
def delete_api(request, id):
    result = delete_from_db(id)
    return Response(result)

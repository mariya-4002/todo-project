from rest_framework.decorators import api_view
from .models import Music

from .serializers.request.create_music import CreateMusicRequestSerializer
from .serializers.request.update_music import UpdateMusicRequestSerializer
from .serializers.request.get_music import GetMusicRequestSerializer
from .serializers.request.delete_music import DeleteMusicRequestSerializer
from .util.response import error_response


@api_view(['POST'])
def create_music(request):
    serializer = CreateMusicRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    return Music.create_music(serializer.validated_data)


@api_view(['PUT'])
def update_music(request):
    serializer = UpdateMusicRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = serializer.validated_data
    return Music.update_music(data["id"], data)


@api_view(['GET'])
def get_music(request):
    serializer = GetMusicRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    return Music.get_music(serializer.validated_data["id"])


@api_view(['GET'])
def get_all_music(request):
    return Music.get_all_music()


@api_view(['DELETE'])
def delete_music(request):
    serializer = DeleteMusicRequestSerializer(
        data=request.query_params or request.data
    )

    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    return Music.delete_music(serializer.validated_data["id"])

from rest_framework.decorators import api_view
from .models import Music
from . import views

from feature.common.response import error_400, error_404
from feature.common.pagination import paginate_queryset

from .serializers.request.create_music import CreateMusicRequestSerializer
from .serializers.request.update_music import UpdateMusicRequestSerializer
from .serializers.request.get_music import GetMusicRequestSerializer
from .serializers.request.get_all_music import GetAllMusicRequestSerializer
from .serializers.request.delete_music import DeleteMusicRequestSerializer


@api_view(['POST'])
def create_music(request):
    serializer = CreateMusicRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    music = Music.create_music(serializer.validated_data)
    return views.music_created_response(music)


@api_view(['PUT'])
def update_music(request):
    serializer = UpdateMusicRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    music = Music.update_music(
        serializer.validated_data["id"],
        serializer.validated_data
    )

    if not music:
        return error_404()

    return views.music_updated_response(music)


@api_view(['GET'])
def get_music(request):
    serializer = GetMusicRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    music = Music.get_music(serializer.validated_data["id"])

    if not music:
        return error_404()

    return views.music_fetched_response(music)


@api_view(['GET'])
def get_all_music(request):
    serializer = GetAllMusicRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return error_400(serializer.errors)

    page = serializer.validated_data["page"]
    limit = serializer.validated_data["limit"]

    queryset = Music.get_all_music()
    paginated = paginate_queryset(queryset, page=page, limit=limit)

    paginated["results"] = [
        {
            "id": m.id,
            "title": m.title,
            "artist": {
                "id": m.artist.id,
                "name": m.artist.name
            }
        }
        for m in paginated["results"]
    ]

    return views.music_list_response(paginated)



@api_view(['DELETE'])
def delete_music(request):
    serializer = DeleteMusicRequestSerializer(
        data=request.query_params or request.data
    )

    if not serializer.is_valid():
        return error_400(serializer.errors)

    deleted = Music.delete_music(serializer.validated_data["id"])

    if not deleted:
        return error_404()

    return views.music_deleted_response()

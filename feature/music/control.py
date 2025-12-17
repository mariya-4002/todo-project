from rest_framework.decorators import api_view
from .serializers import MusicSerializer
from .dataclass import MusicData
from .models import Music
from .util.response import (
    success_response,
    error_response,
    paginate_queryset
)


# ---------------- CREATE ----------------
@api_view(['POST'])
def create_music(request):
    serializer = MusicSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response(serializer.errors)

    music_data = MusicData(**serializer.validated_data)
    music = Music.create_music(music_data)

    return success_response({
        "id": music.id,
        "title": music.title,
        "artist": music.artist
    })


# ---------------- UPDATE ----------------
@api_view(['PUT'])
def update_music(request):
    music_id = request.data.get("id")
    if not music_id:
        return error_response("music_id is required")

    serializer = MusicSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response(serializer.errors)

    try:
        music_data = MusicData(**serializer.validated_data)
        music = Music.update_music(music_id, music_data)

        return success_response({
            "id": music.id,
            "title": music.title,
            "artist": music.artist
        })

    except Music.DoesNotExist:
        return error_response("Music not found")



# ---------------- GET ONE ----------------
@api_view(['GET'])
def get_music(request):
    music_id = request.GET.get("id")
    if not music_id:
        return error_response("music_id is required")

    try:
        music = Music.get_music(music_id)

        return success_response({
            "id": music.id,
            "title": music.title,
            "artist": music.artist
        })

    except Music.DoesNotExist:
        return error_response("Music not found")



# ---------------- GET ALL (WITH PAGINATION) ----------------
@api_view(['GET'])
def get_all_music(request):
    music_list = Music.get_all_music()

    # convert queryset to list of dicts
    data = []
    for music in music_list:
        data.append({
            "id": music.id,
            "title": music.title,
            "artist": music.artist
        })

    paginated_data, meta = paginate_queryset(data, request)

    return success_response(paginated_data, meta)


# ---------------- DELETE ----------------
@api_view(['DELETE'])
def delete_music(request):
    music_id = request.data.get("id") or request.GET.get("id")

    if not music_id:
        return error_response("music_id is required")

    try:
        Music.delete_music(music_id)
        return success_response("Music deleted successfully")

    except Music.DoesNotExist:
        return error_response("Music not found")



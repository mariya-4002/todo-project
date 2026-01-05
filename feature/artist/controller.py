from rest_framework.decorators import api_view
from feature.common.response import error_400, error_404
from feature.common.pagination import paginate_queryset

from .models import Artist
from . import views

from .serializers.request.create_artist import CreateArtistRequestSerializer
from .serializers.request.update_artist import UpdateArtistRequestSerializer
from .serializers.request.get_artist import GetArtistRequestSerializer
from .serializers.request.get_all_artist import GetAllArtistRequestSerializer
from .serializers.request.delete_artist import DeleteArtistRequestSerializer


@api_view(['POST'])
def create_artist(request):
    serializer = CreateArtistRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_400(serializer.errors)

    artist = Artist.create_artist(serializer.validated_data)
    return views.artist_created_response(artist)


@api_view(['PUT'])
def update_artist(request):
    serializer = UpdateArtistRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_400(serializer.errors)

    artist = Artist.update_artist(
        serializer.validated_data["id"],
        serializer.validated_data
    )

    if not artist:
        return error_404()

    return views.artist_updated_response(artist)


@api_view(['GET'])
def get_artist(request):
    serializer = GetArtistRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return error_400(serializer.errors)

    artist = Artist.get_artist(serializer.validated_data["id"])
    if not artist:
        return error_404()

    return views.artist_fetched_response(artist)


@api_view(['GET'])
def get_all_artist(request):
    serializer = GetAllArtistRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return error_400(serializer.errors)

    page = serializer.validated_data["page"]
    limit = serializer.validated_data["limit"]

    queryset = Artist.get_all_artist()
    paginated = paginate_queryset(queryset, page, limit)

    paginated["results"] = [
        {
            "id": a.id,
            "name": a.name,
            "genre": a.genre
        }
        for a in paginated["results"]
    ]

    return views.artist_list_response(paginated)


@api_view(['DELETE'])
def delete_artist(request):
    serializer = DeleteArtistRequestSerializer(
        data=request.query_params or request.data
    )

    if not serializer.is_valid():
        return error_400(serializer.errors)

    deleted = Artist.delete_artist(serializer.validated_data["id"])
    if not deleted:
        return error_404()

    return views.artist_deleted_response()

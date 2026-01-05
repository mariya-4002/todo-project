from rest_framework import status
from feature.common.response import success_response


def artist_created_response(artist):
    return success_response(
        message="Artist created successfully",
        data={
            "id": artist.id,
            "name": artist.name,
            "genre": artist.genre
        },
        status_code=status.HTTP_201_CREATED
    )


def artist_updated_response(artist):
    return success_response(
        message="Artist updated successfully",
        data={
            "id": artist.id,
            "name": artist.name,
            "genre": artist.genre
        }
    )


def artist_fetched_response(artist):
    return success_response(
        data={
            "id": artist.id,
            "name": artist.name,
            "genre": artist.genre
        }
    )


def artist_list_response(data):
    return success_response(data=data)


def artist_deleted_response():
    return success_response(message="Artist deleted successfully")

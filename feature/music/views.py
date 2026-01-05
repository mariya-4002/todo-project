from rest_framework import status
from feature.common.response import success_response


def music_created_response(music):
    return success_response(
        message="Music created successfully",
        data={
            "id": music.id,
            "title": music.title,
            "artist": {
                "id": music.artist.id,
                "name": music.artist.name
            }
        },
        status_code=status.HTTP_201_CREATED
    )


def music_updated_response(music):
    return success_response(
        message="Music updated successfully",
        data={
            "id": music.id,
            "title": music.title,
            "artist": {
                "id": music.artist.id,
                "name": music.artist.name
            }
        }
    )


def music_fetched_response(music):
    return success_response(
        data={
            "id": music.id,
            "title": music.title,
            "artist": {
                "id": music.artist.id,
                "name": music.artist.name
            }
        }
    )


def music_list_response(data):
    return success_response(data=data)


def music_deleted_response():
    return success_response(message="Music deleted successfully")

from .models import Music


def create_in_db(data):
    music = Music.objects.create(
        title=data.title,
        artist=data.artist
    )
    return {
        "id": music.id,
        "message": "Music created"
    }


def update_in_db(music_id, data):
    try:
        music = Music.objects.get(id=music_id)
        music.title = data.title
        music.artist = data.artist
        music.save()
        return {
            "message": "Music updated"
        }
    except Music.DoesNotExist:
        return {
            "error": "Music not found"
        }


def get_from_db(music_id):
    try:
        music = Music.objects.get(id=music_id)
        return {
            "id": music.id,
            "title": music.title,
            "artist": music.artist
        }
    except Music.DoesNotExist:
        return {
            "error": "Music not found"
        }


def get_all_from_db():
    return list(
        Music.objects.all().values(
            "id",
            "title",
            "artist"
        )
    )


def delete_from_db(music_id):
    try:
        Music.objects.get(id=music_id).delete()
        return {
            "message": "Music deleted"
        }
    except Music.DoesNotExist:
        return {
            "error": "Music not found"
        }

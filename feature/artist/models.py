from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    @staticmethod
    def create_artist(data):
        return Artist.objects.create(**data)

    @staticmethod
    def update_artist(artist_id, data):
        try:
            artist = Artist.objects.get(id=artist_id)
            artist.name = data.get("name", artist.name)
            artist.genre = data.get("genre", artist.genre)
            artist.save()
            return artist
        except Artist.DoesNotExist:
            return None

    @staticmethod
    def get_artist(artist_id):
        try:
            return Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            return None

    @staticmethod
    def get_all_artist():
        return Artist.objects.all().order_by("-id")

    @staticmethod
    def delete_artist(artist_id):
        try:
            Artist.objects.get(id=artist_id).delete()
            return True
        except Artist.DoesNotExist:
            return False

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from feature.artist.models import Artist


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="musics"
    )

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

    @classmethod
    def create_music(cls, data):
        artist = Artist.objects.get(id=data["artist_id"])
        return cls.objects.create(
            title=data["title"],
            artist=artist
        )

    @classmethod
    def update_music(cls, music_id, data):
        try:
            music = cls.objects.get(id=music_id)

            if "title" in data:
                music.title = data["title"]

            if "artist_id" in data:
                music.artist = Artist.objects.get(id=data["artist_id"])

            music.save()
            return music
        except (ObjectDoesNotExist, Artist.DoesNotExist):
            return None

    @classmethod
    def get_music(cls, music_id):
        try:
            return cls.objects.get(id=music_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_all_music(cls):
        return cls.objects.all().order_by("-id")

    @classmethod
    def delete_music(cls, music_id):
        try:
            cls.objects.get(id=music_id).delete()
            return True
        except ObjectDoesNotExist:
            return False

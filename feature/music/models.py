from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.artist}"

    @classmethod
    def create_music(cls, data):
        return cls.objects.create(
            title=data["title"],
            artist=data["artist"]
        )

    @classmethod
    def update_music(cls, music_id, data):
        try:
            music = cls.objects.get(id=music_id)
            music.title = data["title"]
            music.artist = data["artist"]
            music.save()
            return music
        except ObjectDoesNotExist:
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

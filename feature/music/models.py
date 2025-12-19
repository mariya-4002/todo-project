from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .util.response import success_response, error_response


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.artist}"

    # ---------------- CREATE ----------------
    @classmethod
    def create_music(cls, data: dict):
        try:
            music = cls.objects.create(
                title=data["title"],
                artist=data["artist"]
            )

            return success_response(
                message="Music created successfully",
                data={
                    "id": music.id,
                    "title": music.title,
                    "artist": music.artist
                },
                status_code=201
            )

        except Exception as e:
            return error_response(
                message=str(e),
                status_code=400
            )

    # ---------------- UPDATE ----------------
    @classmethod
    def update_music(cls, music_id: int, data: dict):
        try:
            music = cls.objects.get(id=music_id)
            music.title = data["title"]
            music.artist = data["artist"]
            music.save()

            return success_response(
                message="Music updated successfully",
                data={
                    "id": music.id,
                    "title": music.title,
                    "artist": music.artist
                }
            )

        except ObjectDoesNotExist:
            return error_response(
                message="Music not found",
                status_code=404
            )

    # ---------------- GET ONE ----------------
    @classmethod
    def get_music(cls, music_id: int):
        try:
            music = cls.objects.get(id=music_id)

            return success_response(
                message="Music fetched successfully",
                data={
                    "id": music.id,
                    "title": music.title,
                    "artist": music.artist
                }
            )

        except ObjectDoesNotExist:
            return error_response(
                message="Music not found",
                status_code=404
            )

    # ---------------- GET ALL ----------------
    @classmethod
    def get_all_music(cls):
        queryset = cls.objects.all().order_by("-id")

        data = [
            {
                "id": music.id,
                "title": music.title,
                "artist": music.artist
            }
            for music in queryset
        ]

        return success_response(
            message="Music list fetched successfully",
            data=data
        )

    # ---------------- DELETE ----------------
    @classmethod
    def delete_music(cls, music_id: int):
        try:
            music = cls.objects.get(id=music_id)
            music.delete()

            return success_response(
                message="Music deleted successfully"
            )

        except ObjectDoesNotExist:
            return error_response(
                message="Music not found",
                status_code=404
            )

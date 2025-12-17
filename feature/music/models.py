from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    # -------- CREATE --------
    @classmethod
    def create_music(cls, music_data):
        return cls.objects.create(
            title=music_data.title,
            artist=music_data.artist
        )

    # -------- UPDATE --------
    @classmethod
    def update_music(cls, music_id, music_data):
        music = cls.objects.get(id=music_id)
        music.title = music_data.title
        music.artist = music_data.artist
        music.save()
        return music

    # -------- GET ONE --------
    @classmethod
    def get_music(cls, music_id):
        return cls.objects.get(id=music_id)

    # -------- GET ALL --------
    @classmethod
    def get_all_music(cls):
        return cls.objects.all()

    # -------- DELETE --------
    @classmethod
    def delete_music(cls, music_id):
        music = cls.objects.get(id=music_id)
        music.delete()

from rest_framework import serializers
from feature.artist.models import Artist


class CreateMusicRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    artist_id = serializers.IntegerField()

    def validate_artist_id(self, value):
        if not Artist.objects.filter(id=value).exists():
            raise serializers.ValidationError("Artist not found")
        return value

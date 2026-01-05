from rest_framework import serializers
from feature.artist.models import Artist


class UpdateMusicRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100, required=False)
    artist_id = serializers.IntegerField(required=False)

    def validate_artist_id(self, value):
        if not Artist.objects.filter(id=value).exists():
            raise serializers.ValidationError("Artist not found")
        return value

from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    artist = serializers.CharField(max_length=100)

    # -------- VALIDATION --------
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Title must be at least 2 characters"
            )
        return value

    def validate_artist(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Artist name must be at least 2 characters"
            )
        return value

    # -------- CREATE --------
    def create(self, validated_data):
        """
        Create a new Music record
        """
        return Music.objects.create(
            title=validated_data['title'],
            artist=validated_data['artist']
        )

    # -------- UPDATE --------
    def update(self, instance, validated_data):
        """
        Update an existing Music record
        """
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.save()
        return instance

from rest_framework import serializers

class CreateMusicRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    artist = serializers.CharField(max_length=100)

    def validate_title(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Title must have at least 2 characters")
        return value

    def validate_artist(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Artist must have at least 2 characters")
        return value

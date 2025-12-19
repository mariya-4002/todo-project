from rest_framework import serializers

class UpdateMusicRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    artist = serializers.CharField(max_length=100)

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid music id")
        return value

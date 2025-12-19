from rest_framework import serializers

class DeleteMusicRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid music id")
        return value

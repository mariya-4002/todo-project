from rest_framework import serializers

class GetAllMusicRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)

    def validate_page(self, value):
        if value <= 0:
            raise serializers.ValidationError("Page must be greater than 0")
        return value

    def validate_limit(self, value):
        if value <= 0:
            raise serializers.ValidationError("Limit must be greater than 0")
        return value

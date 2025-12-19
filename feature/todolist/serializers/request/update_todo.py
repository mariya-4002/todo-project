from rest_framework import serializers

class UpdateTodoRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid todo id")
        return value

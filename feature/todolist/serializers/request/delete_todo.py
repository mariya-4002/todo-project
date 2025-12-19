from rest_framework import serializers

class DeleteTodoRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Invalid todo id")
        return value

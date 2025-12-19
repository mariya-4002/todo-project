from rest_framework import serializers

class DeleteTodoResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

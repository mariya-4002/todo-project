from rest_framework import serializers


class GetAllTodoRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)

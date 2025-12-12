from rest_framework import serializers

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

class TodoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.CharField()

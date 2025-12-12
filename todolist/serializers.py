from rest_framework import serializers

class TodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)


class TodoIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

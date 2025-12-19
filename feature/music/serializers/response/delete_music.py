from rest_framework import serializers

class DeleteMusicResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

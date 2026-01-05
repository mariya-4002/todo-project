from rest_framework import serializers


class DeleteArtistResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

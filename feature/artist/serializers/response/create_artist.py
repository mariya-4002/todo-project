from rest_framework import serializers


class CreateArtistResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genre = serializers.CharField()

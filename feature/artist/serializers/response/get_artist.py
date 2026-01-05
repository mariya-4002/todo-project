from rest_framework import serializers


class GetArtistResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genre = serializers.CharField()

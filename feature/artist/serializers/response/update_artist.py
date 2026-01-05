from rest_framework import serializers


class UpdateArtistResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genre = serializers.CharField()

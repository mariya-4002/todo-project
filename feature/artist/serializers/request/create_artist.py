from rest_framework import serializers


class CreateArtistRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)

from rest_framework import serializers


class ArtistItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genre = serializers.CharField()


class GetAllArtistResponseSerializer(serializers.Serializer):
    page = serializers.IntegerField()
    limit = serializers.IntegerField()
    total = serializers.IntegerField()
    results = ArtistItemSerializer(many=True)

from rest_framework import serializers


class UpdateArtistRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, required=False)
    genre = serializers.CharField(max_length=100, required=False)

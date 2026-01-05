from rest_framework import serializers


class GetArtistRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

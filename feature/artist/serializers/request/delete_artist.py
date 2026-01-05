from rest_framework import serializers


class DeleteArtistRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

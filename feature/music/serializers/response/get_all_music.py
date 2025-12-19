from rest_framework import serializers

class GetAllMusicResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    artist = serializers.CharField()

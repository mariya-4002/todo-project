from rest_framework import serializers

class GetMusicResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    artist = serializers.CharField()

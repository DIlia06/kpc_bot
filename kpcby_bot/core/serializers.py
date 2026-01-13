from rest_framework import serializers

class AboutUsSerializer(serializers.Serializer):
    text = serializers.CharField()
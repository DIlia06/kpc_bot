from rest_framework import serializers


class BaseProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    link = serializers.CharField()

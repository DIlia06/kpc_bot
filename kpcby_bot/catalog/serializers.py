from rest_framework import serializers


class CatalogSerializer(serializers.Serializer):
    name = serializers.CharField()
    link = serializers.CharField()

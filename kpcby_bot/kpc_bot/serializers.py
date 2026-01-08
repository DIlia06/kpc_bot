from rest_framework import serializers

from kpc_bot.models import UserAppeal


class AboutUsSerializer(serializers.Serializer):
    text = serializers.CharField()


class UserAppealsSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    message = serializers.CharField()

    def create(self, validated_data):
        return UserAppeal.objects.create(**validated_data)

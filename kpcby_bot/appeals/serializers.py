from rest_framework import serializers

from appeals.models import UserAppeal

class UserAppealsSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    message = serializers.CharField()

    def create(self, validated_data):
        return UserAppeal.objects.create(**validated_data)
from rest_framework import serializers

from appeals.models import UserAppeal


# class UserAppealsSerializer(serializers.Serializer):
#     telegram_id = serializers.PrimaryKeyRelatedField(
#         queryset=TelegramUser.objects.all()
#     )
#     theme = serializers.CharField()
#     message = serializers.CharField()
#     status = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return UserAppeal.objects.create(**validated_data)

class CreateUserAppealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppeal
        fields = ['user', 'theme', 'message', 'status']

# {
#     "user": 1,
#     "theme": "test",
#     "message": "tesssttest",
#     "status": 0
# }
# http://127.0.0.1:8000/api/appeals/create_appeal
"""--------------------------------------------------------------------------------"""


class DetailUserAppealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppeal
        fields = ['user', 'theme', 'message', 'status']


class ListUserAppealsSerializer(serializers.Serializer):
    user = serializers.CharField(source='user.telegram_id')  # берём telegram_id из связанной модели
    message = serializers.CharField()

from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from appeals.serializers import UserAppealsSerializer


class CreateUserAppeal(APIView):
    def post(self, request: Request) -> Response:
        user_message = request.data.get('message', '').lower()

        if user_message in ['какой ваш адрес?', 'где вы находитесь?', 'где вы?', 'какой адрес?', 'где расположение?']:
            return Response({"response": "Мы находимся по адресу: город Минск, улица Олешева 3, офис 323"})

        serializer = UserAppealsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

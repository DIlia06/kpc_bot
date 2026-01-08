
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from kpc_bot.models import AboutUs, UserAppeal
from kpc_bot.serializers import AboutUsSerializer, UserAppealsSerializer


class AboutUsView(APIView):
    def get(self, request: Request) -> Response:
        aboutus_info = AboutUs.objects.first()
        serializer = AboutUsSerializer(instance=aboutus_info)
        return Response(serializer.data)


class UserAppealListView(APIView):
    def get(self, request: Request) -> Response:
        appeals = UserAppeal.objects.all()
        serializer = UserAppealsSerializer(appeals, many=True)
        return Response(serializer.data)


class CreateUserAppeal(APIView):
    def post(self, request: Request) -> Response:
        user_message = request.data.get('message', '').lower()

        if user_message in ['какой ваш адрес?', 'где вы находитесь?', 'где вы?', 'какой адрес?', 'где расположение?']:
            return Response({"response": "Мы находимся по адресу: город Минск, улица Олешева 3, офис 323"})

        serializer = UserAppealsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)







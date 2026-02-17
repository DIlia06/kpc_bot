from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from appeals.models import UserAppeal
from appeals.serializers import CreateUserAppealsSerializer, DetailUserAppealsSerializer, ListUserAppealsSerializer


class CreateUserAppeal(APIView):
    def post(self, request: Request) -> Response:
        serializer = CreateUserAppealsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ListUserAppeals(APIView):
    def get(self, request: Request) -> Response:
        appeals = UserAppeal.objects.all()
        serializer = ListUserAppealsSerializer(appeals, many=True)
        return Response(serializer.data)


class DetailUserAppeals(APIView):
    def get(self, request: Request, pk: int) -> Response:
        appeal = UserAppeal.objects.get(pk=pk)
        serializer = DetailUserAppealsSerializer(instance=appeal)
        return Response(serializer.data)

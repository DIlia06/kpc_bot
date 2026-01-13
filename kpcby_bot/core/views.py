from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import AboutUs
from core.serializers import AboutUsSerializer


class AboutUsView(APIView):
    def get(self, request: Request) -> Response:
        aboutus_info = AboutUs.objects.first()
        serializer = AboutUsSerializer(instance=aboutus_info)
        return Response(serializer.data)

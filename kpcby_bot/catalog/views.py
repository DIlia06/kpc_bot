from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CatalogView(APIView):
    def get(self, request: Request) -> Response:
        pass
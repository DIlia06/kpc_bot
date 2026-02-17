from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Printers, Mfu, OptionalEquipment, Consumables, Spares, RelatedProducts
from catalog.serializers import CatalogSerializer


class BaseCategoryListView(APIView):
    model = None

    def get(self, request: Request) -> Response:
        queryset = self.model.objects.all()
        serializer = CatalogSerializer(queryset, many=True)
        return Response(serializer.data)

class PrintersListView(BaseCategoryListView):
    model = Printers

class MfuListView(BaseCategoryListView):
    model = Mfu

class OptionalEquipmentListView(BaseCategoryListView):
    model = OptionalEquipment

class ConsumablesListView(BaseCategoryListView):
    model = Consumables

class SparesListView(BaseCategoryListView):
    model = Spares

class RelatedProductsListView(BaseCategoryListView):
    model = RelatedProducts

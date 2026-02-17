from django.urls import path

from catalog.views import BaseCategoryListView, RelatedProductsListView, SparesListView, ConsumablesListView, \
    OptionalEquipmentListView, MfuListView, PrintersListView

urlpatterns = [
    path('printers', PrintersListView.as_view()),
    path('mfu', MfuListView.as_view()),
    path('optional', OptionalEquipmentListView.as_view()),
    path('consumables', ConsumablesListView.as_view()),
    path('spares', SparesListView.as_view()),
    path('related', RelatedProductsListView.as_view()),
    path('all', BaseCategoryListView.as_view()),
]
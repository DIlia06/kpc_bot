from django.urls import path
from .views import GetOrCreateUserView

urlpatterns = [
    path('get_or_create', GetOrCreateUserView.as_view()),
]
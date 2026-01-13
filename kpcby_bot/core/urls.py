from django.urls import path

from core.views import AboutUsView

urlpatterns = [
    path('about_us', AboutUsView.as_view())
]
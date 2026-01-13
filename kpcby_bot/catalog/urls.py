from django.urls import path


urlpatterns = [
    path('about_us', AboutUsView.as_view())
]
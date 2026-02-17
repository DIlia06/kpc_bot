from django.urls import path

from appeals.views import CreateUserAppeal, ListUserAppeals, DetailUserAppeals

urlpatterns = [
    path('create_appeal', CreateUserAppeal.as_view()),
    path('list', ListUserAppeals.as_view()),
    path('<int:pk>', DetailUserAppeals.as_view()),
]
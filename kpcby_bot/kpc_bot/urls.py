from django.urls import path

from kpc_bot.views import AboutUsView, CreateUserAppeal, UserAppealListView

urlpatterns = [
    path('aboutus', AboutUsView.as_view()),
    path('appeal', CreateUserAppeal.as_view()),
    path('appeals', UserAppealListView.as_view()),

    path('catalog', UserAppealListView.as_view()),
    # при нажатии на кнопку каталог появляются много кнопок принтеры мфу опциональное обслуживание

]
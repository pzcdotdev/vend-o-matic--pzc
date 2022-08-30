from django.urls import path
from api import views

urlpatterns = [
    path('', views.CoinViewSet.as_view(), name='coin')
]
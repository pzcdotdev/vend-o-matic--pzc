from django.urls import path
from api import views

urlpatterns = [
    path('', views.CoinViewSet.as_view(), name='coin'),
    path('inventory', views.InventoryViewSet.as_view(), name='inventory'),
    path('inventory/<int:id>', views.InventoryViewSet.as_view(), name='inventory'),
]
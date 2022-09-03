from api import views
from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="index"),
    path("coinslot", views.CoinViewSet.as_view(), name="coinslot"),
    path("inventory", views.InventoryViewSet.as_view(), name="inventory"),
    path("inventory/<int:id>", views.InventoryViewSet.as_view(), name="inventory"),
]

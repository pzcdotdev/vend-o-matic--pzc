from api import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drinkmachine.views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("coinslot", views.CoinViewSet.as_view(), name="coinslot"),
    path("inventory", views.InventoryViewSet.as_view(), name="inventory"),
    path("inventory/<int:id>", views.InventoryViewSet.as_view(), name="inventory"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from api import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # This is data we want to share with react
        context["sharedData"] = {"first_name": "paul", "message": "hi there!"}

        return context


urlpatterns = [
    path("", IndexView.as_view(template_name="base.html"), name="index"),
    path("coinslot", views.CoinViewSet.as_view(), name="coinslot"),
    path("inventory", views.InventoryViewSet.as_view(), name="inventory"),
    path("inventory/<int:id>", views.InventoryViewSet.as_view(), name="inventory"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

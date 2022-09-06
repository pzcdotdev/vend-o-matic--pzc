from django.views.generic import TemplateView
from api.models import InventoryModel, CoinModel


class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["initialData"] = {
            "initial_inventory": [
                {"quantity": drink.quantity, "type": drink.type}
                for drink in InventoryModel.objects.all()
            ],
            "initial_coin_count": CoinModel.objects.first().coin,
        }

        return context

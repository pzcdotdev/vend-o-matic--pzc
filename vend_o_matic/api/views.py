from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CoinSerializer
from api.models import CoinModel, InventoryModel


def get_current_coins():
    return CoinModel.objects.first().coin


def update_coin_quantity(addend):
    c = CoinModel.objects.first()
    c.coin += addend
    c.save()


class CoinViewSet(APIView):
    def put(self, request):
        if not request.data["coin"] == 1:
            return Response(
                data={"error": "Please insert a single coin."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            update_coin_quantity(1)
            return Response(
                serializer.data,
                status=status.HTTP_204_NO_CONTENT,
                headers={"X-Coins": f"{get_current_coins()}"},
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if get_current_coins() <= 0:
            return Response(
                data={"error": "No coins in machine."}, status=status.HTTP_404_NOT_FOUND
            )
        update_coin_quantity(-1)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            headers={"X-Coins": f"{get_current_coins()}"},
        )


class InventoryViewSet(APIView):
    def get(self, request):
        inventory = [drink.quantity for drink in InventoryModel.objects.all()]

        return Response(inventory)

    def put(self, request, id):
        if get_current_coins() < 2:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                headers={"X-Coins": f"{get_current_coins()}"},
            )

        try:
            drink_choice = InventoryModel.objects.get(id=id)
        except InventoryModel.DoesNotExist:
            return Response(
                data={"error": "choice id not found"}, status=status.HTTP_404_NOT_FOUND
            )

        choice_quantity = drink_choice.quantity
        if choice_quantity == 0:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                headers={"X-Coins": f"{get_current_coins()}"},
            )

        drink_choice.quantity -= 1
        drink_choice.save()

        update_coin_quantity(-2)
        headers = {
            "X-Coins": f"{get_current_coins()}",
            "X-Inventory-Remaining": f"{drink_choice.quantity}",
        }
        update_coin_quantity(-(get_current_coins()))

        return Response(
            data={"quantity": 1}, status=status.HTTP_200_OK, headers=headers
        )

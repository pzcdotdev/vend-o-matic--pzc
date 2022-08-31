from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CoinSerializer
from api.models import CoinModel, InventoryModel

class CoinViewSet(APIView):
    def update_coin_quantity(self, addend):
        c = CoinModel.objects.first()
        c.coin += addend
        c.save()

    def get_current_coins(self):
        return CoinModel.objects.first().coin

    def get_headers(self):
        return {
            "X-Coins": f'{self.get_current_coins()}'
        }

    def put(self, request):
        if not request.data['coin'] == 1:
            return Response(data={'error': 'Please insert a single coin.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            self.update_coin_quantity(1)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT, 
            headers=self.get_headers())
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if self.get_current_coins() <= 0:
            return Response(data={'error': 'No coins in machine.'}, status=status.HTTP_404_NOT_FOUND)
        self.update_coin_quantity(-1)
        return Response(status=status.HTTP_204_NO_CONTENT, 
                        headers=self.get_headers())


class InventoryViewSet(APIView):
    def get(self, request):
        inventory = [drink.quantity for drink in InventoryModel.objects.all()]
        
        return Response(inventory)

    def put(self, request, id):
        # check quantity of coins is 2 or greater
            # return 403 if not
        # check requested beverage id quantity is greater than 0
            # return 404 if not
        # decrement drink quantity
        # decrement quarter quantity by 2
        # return 200 with body, returned coins, remaining drink inventory
        return Response(data={"purchasing": id}, status=status.HTTP_200_OK)

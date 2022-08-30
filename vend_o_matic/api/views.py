from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CoinSerializer
from api.models import CoinModel, InventoryModel

class CoinViewSet(APIView):
    def get_current_coins(self):
        return CoinModel.objects.all().count()

    def get_headers(self):
        return {
            "X-Coins": f'{self.get_current_coins()}'
        }

    def put(self, request):
        if not request.data['coin'] == 1:
            return Response(data={'error': 'Please insert a single coin.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT, 
            headers=self.get_headers())
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            coin = CoinModel.objects.latest('id')
        except CoinModel.DoesNotExist:
            return Response(data={'error': 'No coins in machine.'}, status=status.HTTP_404_NOT_FOUND)

        coin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, 
                        headers=self.get_headers())


class InventoryViewSet(APIView):
    def get(self, request):
        inventory = InventoryModel.objects.all()
        return Response(inventory)

        

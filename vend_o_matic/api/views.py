from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CoinSerializer
from api.models import CoinModel

class CoinViewSet(APIView):

    def put(self, request):
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            coin = CoinModel.objects.latest('id')
        except CoinModel.DoesNotExist:
            raise Http404

        coin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

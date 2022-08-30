from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import QuarterSerializer

class QuarterViewSet(APIView):

    def put(self, request):
        serializer = QuarterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


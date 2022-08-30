from rest_framework import serializers
from api.models import CoinModel

class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinModel
        fields = ('coin',)
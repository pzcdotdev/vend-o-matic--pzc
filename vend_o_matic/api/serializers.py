from rest_framework import serializers
from api.models import CoinModel, InventoryModel

class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinModel
        fields = ('coin',)


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryModel
        fields = ('type',)
from django.db import models


class CoinModel(models.Model):
    coin = models.IntegerField()


class InventoryModel(models.Model):
    type = models.CharField(
        max_length=15
    )
    quantity = models.IntegerField()
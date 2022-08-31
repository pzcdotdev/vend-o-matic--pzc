from django.db import models


class CoinModel(models.Model):
    coin = models.IntegerField()


class InventoryModel(models.Model):
    class DrinkChoices(models.TextChoices):
        BUTTERBEER = "BB", "Butterbeer"
        ENT_DRAUGHT = "ED", "Ent Draught"
        AMBROSIA = "AB", "Ambrosia"
    
    type = models.CharField(
        max_length=15,
        choices=DrinkChoices.choices
    )
    quantity = models.IntegerField()
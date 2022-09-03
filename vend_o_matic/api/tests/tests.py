import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api import models


class ApiTests(APITestCase):
    def set_coins(self, coins):
        coin = models.CoinModel.objects.last()
        coin.coin = coins
        coin.save()

    def test_coin_put(self):
        url = reverse("coinslot")
        data = {"coin": 1}

        response = self.client.put(
            url, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(response.has_header("X-Coins"))
        self.assertEqual(response.headers["X-Coins"], "1")

    def test_coin_delete(self):
        self.set_coins(5)
        url = reverse("coinslot")

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(response.has_header("X-Coins"))
        self.assertEqual(response.headers["X-Coins"], "4")

    def test_inventory_get(self):
        url = reverse("inventory")
        response_data = [5, 5, 5]

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_data)

    def test_inventory_put_200(self):
        self.set_coins(3)
        url = reverse("inventory", kwargs={"id": "1"})
        response_data = {"quantity": 1}

        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.has_header("X-Coins"))
        self.assertEqual(response.headers["X-Coins"], "1")
        self.assertTrue(response.has_header("X-Inventory-Remaining"))
        self.assertEqual(response.headers["X-Inventory-Remaining"], "4")
        self.assertEqual(response.data, response_data)

    def test_inventory_put_404(self):
        item = models.InventoryModel.objects.get(id=1)
        item.quantity = 0
        item.save()
        self.set_coins(3)
        url = reverse("inventory", kwargs={"id": "1"})

        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(response.has_header("X-Coins"))
        self.assertEqual(response.headers["X-Coins"], "3")

    def test_inventory_put_403(self):
        self.set_coins(1)
        url = reverse("inventory", kwargs={"id": "1"})

        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(response.has_header("X-Coins"))
        self.assertEqual(response.headers["X-Coins"], "1")

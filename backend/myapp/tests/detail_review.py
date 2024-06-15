from django.test import TestCase
from rest_framework import status
from django.urls import reverse
#from django.test.client import encode_multipart
#from django.conf import settings as _settings


CREATE_PRODUCT_URL_DETAIL_REVIEW = reverse("myapp:detail_review-list")


class TestMyAppDetailReviewUrls(TestCase):
    def setUp(self):
        self.response = self.client.get(CREATE_PRODUCT_URL_DETAIL_REVIEW, format="json")
        self.data = self.response.json()
        try:
            self.value = self.data["values"][0]
        except IndexError:
            print("Data vacía")

    def test_detail_review_get(self):
        print("Test componente myapp test_detail_review_get")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertIn("values", self.data)
        try:
            self.assertIsInstance(self.value["pos_date"], str)
            self.assertIsInstance(self.value["qualification"], int)
            self.assertIsInstance(self.value["comments"], str)
            self.assertIsInstance(self.value["active"], bool)
        except AttributeError:
            print("El test no corre si no hay datos en el API")
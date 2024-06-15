from django.test import TestCase
from rest_framework import status
from django.urls import reverse
#from django.test.client import encode_multipart
#from django.conf import settings as _settings


CREATE_PRODUCT_URL_REVIEW = reverse("myapp:review-list")


class TestMyAppReviewUrls(TestCase):
    def setUp(self):
        self.response = self.client.get(CREATE_PRODUCT_URL_REVIEW, format="json")
        self.data = self.response.json()
        try:
            self.value = self.data["values"][0]
        except IndexError:
            print("Data vacía")

    def test_review_get(self):
        print("Test componente myapp test_review_get")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertIn("values", self.data)
        try:
            self.assertIsInstance(self.value["id"], int)
            self.assertIsInstance(self.value["reviewer"], str)
            self.assertIsInstance(self.value["text"], str)
            self.assertIsInstance(self.value["labels"], list)
            self.assertIsInstance(self.value["detail"], int)
            self.assertIsInstance(self.value["active"], bool)
        except AttributeError:
            print("El test no corre si no hay datos en el API")
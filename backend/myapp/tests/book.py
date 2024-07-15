from django.test import TestCase # type: ignore
from rest_framework import status # type: ignore
from django.urls import reverse # type: ignore
#from django.test.client import encode_multipart
#from django.conf import settings as _settings


CREATE_PRODUCT_URL_BOOK = reverse("myapp:book-list")


class TestMyAppBookUrls(TestCase):
    def setUp(self):
        self.response = self.client.get(CREATE_PRODUCT_URL_BOOK, format="json")
        self.data = self.response.json()
        try:
            self.value = self.data["values"][0]
        except IndexError:
            print("Data vacía")

    def test_book_get(self):
        print("Test componente myapp test_book_get")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertIn("values", self.data)
        try:
            self.assertIsInstance(self.value["id"], int)
            #if self.value["boletin"] is not None:
            self.assertIsInstance(self.value["title"], str)
            self.assertIsInstance(self.value["author"], str)
            self.assertIsInstance(self.value["summary"], str)
            self.assertIsInstance(self.value["pos_date"], str)
            self.assertIsInstance(self.value["active"], bool)
        except AttributeError:
            print("El test no corre si no hay datos en el API")
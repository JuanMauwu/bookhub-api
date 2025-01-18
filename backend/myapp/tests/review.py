from django.test import TestCase
from rest_framework import status # type: ignore
from django.urls import reverse
from myapp.models import Review

#TEST GET

class ReviewGetAPITest(TestCase):

from rest_framework import serializers
from myapp.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [   # Campos que deseo incluir para serializar
            "id",
            "title",
            "author",
            "summary",
            "pos_date",
            "active",
        ]
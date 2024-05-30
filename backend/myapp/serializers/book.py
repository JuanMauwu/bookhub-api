from rest_framework import serializers

from myapp.models import Book

class BookSerializer(serializers.ModelSerializer):
    #id = serializers.SerializerMethodField(read_only=True)

    #def get_id(self, obj):
        #return obj.fecha

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "summary",
            "pos_date",
            "active",
        ]
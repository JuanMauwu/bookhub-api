from rest_framework import serializers
from myapp.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "book",
            "reviewer",
            "text",
            "labels",
            "detail",
            "active"
        ]
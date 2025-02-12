from rest_framework import serializers
from myapp.models import DetailReview

class DetailReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailReview
        fields = [
            "id",
            "pos_date",
            "qualification",
            "comments",
            "active"
        ]
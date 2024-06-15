from rest_framework import serializers

from myapp.models import DetailReview

class DetailReviewSerializer(serializers.ModelSerializer):
    #id = serializers.SerializerMethodField(read_only=True)

    #def get_id(self, obj):
        #return obj.fecha

    class Meta:
        model = DetailReview
        fields = [
            "id",
            "pos_date",
            "qualification",
            "comments",
            "active"
        ]
from rest_framework import serializers

from myapp.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    #id = serializers.SerializerMethodField(read_only=True)

    #def get_id(self, obj):
        #return obj.fecha

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
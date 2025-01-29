from rest_framework import serializers

from myapp.models import Label

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            "id",
            "name",
            "description",
            "active",
        ]
from rest_framework import serializers

from myapp.models import Label

class LabelSerializer(serializers.ModelSerializer):
    #id = serializers.SerializerMethodField(read_only=True)

    #def get_id(self, obj):
        #return obj.fecha

    class Meta:
        model = Label
        fields = [
            "id",
            "name",
            "description",
            "active",
        ]
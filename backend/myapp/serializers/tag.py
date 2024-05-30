from rest_framework import serializers

from myapp.models import Tag

class TagSerializer(serializers.ModelSerializer):
    #id = serializers.SerializerMethodField(read_only=True)

    #def get_id(self, obj):
        #return obj.fecha

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]
    
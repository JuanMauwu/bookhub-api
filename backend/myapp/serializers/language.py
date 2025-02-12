from rest_framework import serializers
from myapp.models import Language

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = [ 
            "id",
            "name",
            "code",
            "flag",
            "active",
        ]
        
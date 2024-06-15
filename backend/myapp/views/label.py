from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from myapp.models import Label
from myapp.serializers import LabelSerializer


class LabelListAPIView(generics.ListAPIView):
    queryset = Label.objects.filter(active=True)
    serializer_class = LabelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
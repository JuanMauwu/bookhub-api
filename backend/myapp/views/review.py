from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from myapp.models import Review
from myapp.serializers import ReviewSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.filter(active=True)
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
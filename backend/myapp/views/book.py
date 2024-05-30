from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from myapp.models import Book
from myapp.serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.filter(active=True)
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
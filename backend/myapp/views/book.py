from rest_framework import generics, viewsets # type: ignore


# Create your views here.
from rest_framework.response import Response # type: ignore
from myapp.models import Book
from myapp.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
"""
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.filter(active=True)
    serializer_class = BookSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryser()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
"""
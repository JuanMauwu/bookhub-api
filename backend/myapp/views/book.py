from rest_framework import generics, status 
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.response import Response
from myapp.models import Book
from myapp.serializers import BookSerializer
"""
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""
#class BookListCreateAPIView(generics.ListAPIView):
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(active=True)
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        # Obtén la instancia del objeto a actualizar
        instance = self.get_object()
        # No se establece `partial=True`, forzando la actualización completa
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
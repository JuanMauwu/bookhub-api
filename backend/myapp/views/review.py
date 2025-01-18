from rest_framework import generics, status # type: ignore

# Create your views here.
from rest_framework.response import Response # type: ignore
from myapp.models import Review
from myapp.serializers import ReviewSerializer

"""
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
"""

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.filter(active=True)
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
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


"""
class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.filter(active=True)
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
"""
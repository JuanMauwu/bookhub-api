from rest_framework import generics, status # type: ignore

from rest_framework.response import Response # type: ignore
from myapp.models import Publisher
from myapp.serializers import PublisherSerializer

"""
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerialzer
"""
class PublisherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.filter(active=True)
    serializer_class = PublisherSerializer

class PublisherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
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
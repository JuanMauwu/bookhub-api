from rest_framework import generics, status 

# Create your views here.
from rest_framework.response import Response 
from myapp.models import Label
from myapp.serializers import LabelSerializer


class LabelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Label.objects.filter(active=True)
    serializer_class = LabelSerializer

class LabelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
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
from rest_framework import generics, status # type: ignore
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.response import Response # type: ignore
from myapp.models import DetailReview
from myapp.serializers import DetailReviewSerializer


class DetailReviewListCreateAPIView(generics.ListCreateAPIView):              # Get - Post - esta vista permite obtener todos los objetos de un modelo que haya
    queryset = DetailReview.objects.filter(active=True)                       #especificamos o definimos los datos que se manejaran en la vista, en este caso los filtramos por activo
    serializer_class = DetailReviewSerializer                                 #definimos el serializaer con el que trabajaremos para convertir los datos del modelo a JSon o viceversa

class DetailReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):       #GetDetail - Put - Patch - Delete - esta vista o clase se usa para obtener un objeto en especifico y modificarlo o eliminarlo
    queryset = DetailReview.objects.all()
    serializer_class = DetailReviewSerializer
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):                                     
        instance = self.get_object()                                           #obtén la instancia del objeto a actualizar segun la "id" de lookup_field
        serializer = self.get_serializer(instance, data=request.data)          #instanciamos el serializador con los datos proporcionados en la solicitud
        if serializer.is_valid():
            serializer.save()                                                  #si los datos en el serializador son validos guarda los datos actualizados en la db
            return Response(serializer.data, status=status.HTTP_200_OK)        #devuelve los datos actualizados con codigo de estado 200
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #si hay algun error devuelve un codigo de estado 400 bad request y los errores encontrados
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()                                           #obtén la instancia del objeto a actualizar segun la "id" de lookup_field
        instance.delete()                                                      #se elimina la instancia
        return Response(status=status.HTTP_204_NO_CONTENT)                     #devuelve un codigo de estado 204 No content
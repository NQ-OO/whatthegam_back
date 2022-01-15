from rest_framework.views import APIView
from .models import Place
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlaceSerializer
from texts.models import Text
from django.http import HttpResponseRedirect
from django.urls import reverse
from texts import urls
from rest_framework import viewsets


class PlaceAPIView(viewsets.ModelViewSet): #localhost:8000/

    def list(self, request):

        try:
            map_id = request.data['map_id']
            place = Place.objects.get(map_id=map_id)

        except:
            request.method = 'POST'
            serializer = PlaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            
            Place.objects.get(map_id=map_id)
            
        return HttpResponseRedirect(reverse('texts:text_list', args=[map_id])) 





        
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # else:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)
        # return HttpResponseRedirect(reverse('texts:', args=(request.data['map_id'])))
    


    # def post(self, request):
    #     print("debug")
    #     print(request.data)
    #     print(request.method)
    #     serializer = PlaceSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         print("debug#2")
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


        
            


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
        print(request.POST)
        print(request.data)
        map_id = request.data['map_id']
        try:
            place = Place.objects.get(map_id=map_id)

        except:
            serializer = PlaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            
        return HttpResponseRedirect(reverse('texts:text_count', args=[map_id])) 


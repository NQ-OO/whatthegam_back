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
import json


class PlaceAPIView(viewsets.ModelViewSet): #localhost:8000/

    def list(self, request):
        # print('place api view 시작부분')

        data = json.loads(request.body.decode('utf-8'))
        map_id = data.get('map_id', None)
        print(map_id)
        # map_id = request.data['map_id']
        try:
            place = Place.objects.get(map_id=map_id)

        except:
            serializer = PlaceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        print('여기가 맵'+map_id)
            
        return HttpResponseRedirect(reverse('texts:text_count', kwargs={'map_id':map_id})) 


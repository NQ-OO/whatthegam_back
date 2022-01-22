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
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class PlaceAPIView(viewsets.ModelViewSet): #localhost:8000/
    def list(self, request):
        # print('place api view 시작부분')

        data = request.data
        map_id = data.get('map_id', None)
        print(map_id)
        # map_id = request.data['map_id']
        try:
            place = Place.objects.get(map_id=map_id)

        except:
            serializer = PlaceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            
        return HttpResponseRedirect(reverse('texts:text_count', kwargs={'map_id':map_id})) 


from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Text
from .serializers import *
from whatthegam.models import Place
import random

class TextCountAPIView(APIView):

    def get(self, request, map_id):
        place = Place.objects.get(map_id=map_id)
        text_count = Text.objects.filter(written_place=place).count()
        context = {}
        context['text_count'] = text_count
        return Response(context, status=status.HTTP_200_OK)


class TextListAPIView(APIView):

    def get(self, request, map_id):
        try:
            place = Place.objects.get(map_id=map_id)
        except:
            place_serializer = PlaceSerializer(data=request.data)
            if place_serializer.is_valid():
                place_serializer.save()
                
        place = Place.objects.get(map_id=map_id)
        texts = Text.objects.filter(written_place=place)
        if texts:
            serializer = TextSerializer(texts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            msg = {"msg": "낙서가 없는 보드입니다!"}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, map_id):
        place = Place.objects.get(map_id=map_id)
        if place:
            serializer = TextCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user,
                                written_place=place,
                                spin_rate=round(random.uniform(0, 360), 2),
                                x_axis=round(random.uniform(0,100), 2),
                                y_axis=round(random.uniform(0,100), 2))
            
        all_texts = Text.objects.filter(written_place=place)
        if all_texts:
            text_seri = TextSerializer(all_texts, many=True)
            return Response(text_seri.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TextDetailAPIView(APIView):

    def put(self, request, map_id, text_pk):
        place = Place.objects.get(map_id=map_id)
        text = get_object_or_404(Text, id=text_pk)
        serializer = TextCreateSerializer(text, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, written_place=place)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, map_id, text_pk):
        text = Text.objects.get(id=text_pk)
        text.delete()
        msg = {'msg':"낙서가 삭제되었습니다!"}
        return Response(msg, status=status.HTTP_204_NO_CONTENT)


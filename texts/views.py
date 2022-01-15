from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Text
from .serializers import *
from whatthegam.models import Place


class TextListAPIView(APIView):

    def get(self, request, map_id):
        place = Place.objects.get(map_id=map_id)
        texts = Text.objects.filter(written_place=place)
        if texts:
            serializer = TextSerializer(texts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            msg = {"msg": "낙서가 없는 보드입니다!"}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, map_id):
        # try:    

        # except:
        #     context = {}
        #     context['map_id'] = request.data['map_id']
        #     context['name'] = request.data['name']

        #     place_serializer = PlaceSerializer(data=context)
        #     if place_serializer.is_valid():
        #         place_serializer.save()
        # try:
        #     place = Place.objects.get(map_id=map_id)
        # except:
            place = Place.objects.get(map_id=map_id)
            if place:
                serializer = TextCreateSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(author=request.user, written_place=place)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        return Response(status=status.HTTP_204_NO_CONTENT)





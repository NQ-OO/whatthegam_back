from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.fields import CurrentUserDefault
from rest_framework import status
from .models import Text
from .serializers import *
from whatthegam.models import School

class TextListAPIView(APIView):

    def get(self, request, place_pk):
        school = School.objects.get(pk=place_pk)
        texts = Text.objects.filter(written_place=school)
        if texts:
            serializer = TextSerializer(texts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, place_pk):
        school = School.objects.get(id=place_pk)
        if school:
            serializer = TextCreateSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(author=request.user, written_school=school)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class TextDetailAPIView(APIView):

    def get_object(self, text_pk):
        text = get_object_or_404(Text, pk=text_pk)
        return text

    def put(self, request, place_pk, text_pk):
        school = School.objects.get(id=place_pk)
        text = self.get_object(pk=text_pk)
        serializer = TextCreateSerializer(text, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, written_school=school)
            return Response(serializer.data)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, text_pk):
        text = self.get_object(pk=text_pk)
        text.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





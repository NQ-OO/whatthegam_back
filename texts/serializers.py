from rest_framework import serializers
from .models import Text
from whatthegam.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    author_year = serializers.SerializerMethodField(method_name='get_author_year')

    class Meta:
        model = Text
        fields = ('id', 'content', 'created_dt', 'x_axis', 'y_axis', 'author', 'written_place', 'author_year')
    
    def get_author_year(self, obj):
        return obj.author.profile.year


class TextCreateSerializer(serializers.ModelSerializer):
    author_year = serializers.SerializerMethodField(method_name='get_author_year')

    class Meta:
        model = Text
        fields = ('id', 'author', 'content', 'created_dt', 'x_axis', 'y_axis', 'author_year')

    def get_author_year(self, obj):
        return obj.author.profile.year
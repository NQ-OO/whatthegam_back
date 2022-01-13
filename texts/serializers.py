from rest_framework import serializers
from .models import Text

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

class TextCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'content', 'created_dt', 'x_axis', 'y_axis')
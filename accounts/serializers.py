from rest_framework import serializers
from whatthegam.models import School
from .models import Profile




class ProfileSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Profile # quest 모델 사용
    fields = '__all__'
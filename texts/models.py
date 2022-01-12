from django.db import models
from django.contrib.auth.models import User
from whatthegam.models import School
# Create your models here.
class Text(models.Model):
    content = models.TextField() #텍스트 내용
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #작성자
    created_dt = models.DateTimeField(auto_now=True) #작성 시간
    written_place = models.ForeignKey(School, on_delete=models.SET_NULL, null=True) #작성 장소
    x_axis = models.FloatField(default=0.0) # 보드 상의 x축 위치
    y_axis = models.FloatField(default=0.0) # 보드 상의 y축 위치

    def __str__(self):
        return self.content
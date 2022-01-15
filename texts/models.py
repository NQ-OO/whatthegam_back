from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

from whatthegam.models import Place
# Create your models here.
class Text(models.Model):
    content = models.TextField() #텍스트 내용
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) #작성자
    created_dt = models.DateTimeField(auto_now=True) #작성 시간
    written_place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True) #작성 장소
    x_axis = models.FloatField(default=0.0) # 보드 상의 x축 위치
    y_axis = models.FloatField(default=0.0) # 보드 상의 y축 위치

    def __str__(self):
        return self.content






# 아무도 글을 쓴 적 없느는 장소 => Place, Text => 새 글을 쓰시겠습니까? -> yes -> 칠판을 띄워주는
#yes 버튼을 누를 때 Place 모델 쪽으로 POST를 보내서, Place 모델에다가 장소를 저장하

# 칠판을 바로 띄우고, 거기다 글을 쓰면 POST 요청으로 / content 장소이름 장소id 사용자 정보 => 

# 칠판을 띄워주는 거지. 칠판을 띄워는 페이지로 이동할 때, redirect할 때 GET 요청을 보내면 =>데이터가 없음.

# 누가 글을 쓴 적은 있는데, 지워서 현재 글이 없어 = DB에 장소는 있어, 근데 장소에 대한 텍스트는 없는 상태


# 현재 글이 있는 장소드
# 장소도 DB에 있고, 텍스트 있고.

from django.urls import path
from texts import views

app_name = 'texts'

urlpatterns = [
    path('', views.TextListAPIView.as_view(), name='text_list'),
    path('<int:text_pk>/', views.TextDetailAPIView.as_view(), name='text_detail')
]
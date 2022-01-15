from django.urls import path
from texts import views

app_name = 'texts'

urlpatterns = [
    path('count/', views.TextCountAPIView.as_view(), name='text_count'),
    path('texts/', views.TextListAPIView.as_view(), name='text_list'),
    path('texts/<int:text_pk>/', views.TextDetailAPIView.as_view(), name='text_detail')
]
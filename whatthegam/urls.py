"""whatthegam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
# from accounts.views import ProfileViewSet
from whatthegam import views
from users.views import RegistrationAPI

# router = routers.DefaultRouter()
# router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('account/', include('allauth.urls')),
    # path('rest-auth/signup/', include('rest_auth.registration.urls')),
    path('rest-auth/signup/', RegistrationAPI.as_view()),
    # path('rest-auth/profile/', include('accounts.urls')),
    path('api/token/', obtain_auth_token, name = 'obtain-token'), #해당 username 의 token 을 확인할 수 있는 url
    path('<int:map_id>/texts/', include('texts.urls')),
    path('', views.PlaceAPIView.as_view({'get':'list'})),
]

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework import status, generics
# from users.models import AuthToken
from rest_framework.authtoken.models import Token


# # Create your views here.

# class CustomUserListAPIView(APIView):
  
#   def post(request) :
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(username=request.username,  password =request.password, year = request.year)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)


# class SignupView(APIView):
#     def post(self, request):
#         user = CustomUser.objects.create_user(username=request.data['username'], password=request.data['password'], year = request.data['year'])
#         user.save()

#         token = Token.objects.create(user=user)
#         return Response({"Token": token.key})
      
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token.key,
            }
        )
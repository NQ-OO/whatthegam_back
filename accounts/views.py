# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializers import ProfileSerializer
# from .models import Profile
# from rest_framework.views import APIView  
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# # Create your views here.


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
    
#     def update(self, request, pk) :
#         user = User.objects.get(id = pk)
#         queryset = Profile.objects.get(user_id = user.id)
#         queryset.year = request.data.__getitem__('year')
#         serializer = ProfileSerializer(queryset, data=request.data)
#         print(serializer) 
#         if serializer.is_valid():
#             serializer.save(year = queryset.year)
#         result = serializer.data
#         return Response(result)
    
    

# class ProfileView(APIView):
#     """
#     PUT /profile/{user_id}
#     """
#     def put(self, request, user_pk):
#         profile = get_object_or_404(Profile, id=user_pk)
#         serializer = ProfileCreateSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user, written_place=place)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)
        
#         return Response("test ok", status=200)


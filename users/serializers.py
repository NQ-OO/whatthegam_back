from rest_framework import serializers

from users.models import CustomUser


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "year")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data["username"], validated_data["password"], validated_data["year"]
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "year")
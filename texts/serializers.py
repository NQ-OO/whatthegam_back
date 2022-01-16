from rest_framework import serializers
from users.models import CustomUser
from .models import Text
from whatthegam.models import Place


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    author_year = serializers.SerializerMethodField(method_name='get_author_year')
    create_dt = serializers.SerializerMethodField(method_name='get_create_dt')

    class Meta:
        model = Text
        fields = ('id', 'content', 'author', 'create_dt', 'written_place', 'x_axis', 'y_axis', 'spin_rate', 'author_year')
    
    def get_author_year(self, obj):
        return obj.author.year
    
    def get_create_dt(self, obj):
        return obj.created_dt.strftime("%Y-%m-%d %H:%M:%S")


class TextCreateSerializer(serializers.ModelSerializer):
    author_year = serializers.SerializerMethodField(method_name='get_author_year')
    create_dt = serializers.SerializerMethodField(method_name='get_create_dt')

    class Meta:
        model = Text
        fields = ('id', 'content', 'author', 'create_dt', 'written_place', 'x_axis', 'y_axis', 'spin_rate', 'author_year')

    def get_author_year(self, obj):
        print(obj.author)
        return obj.author.year

    def get_create_dt(self, obj):
        return obj.created_dt.strftime("%Y-%m-%d %H:%M:%S")

        
    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     if validated_data['is_private'] == False:
    #         instance = self.Meta.model(**validated_data)
    #         if instance:
    #             instance.save()
    #         return instance
    #     else:
    #         if validated_data['users_opened']:
    #             print(validated_data)
    #             users = validated_data.pop('users_opened')
    #             print(validated_data)
    #             print(users)
    #             user_ids = [user.id for user in users]
    #             print(type(users[0]))
    #             instance = self.Meta.model(**validated_data)
    #             if instance:
    #                 instance.save()
    #                 for user in users:
    #                     instance.users_opened.add(user)
    #             return instance

    # def create(self, validated_data):
    #     print("debug#3")
    #     print(validated_data)
    #     user = validated_data.pop('users_opened')
    #     print(user)
    #     text = Text.objects.create(**validated_data)
    #     print(text)
    #     print(text.users_opened)
    #     text.users_opened.add(user)
    #     print(text.users_opened)

    #     return text
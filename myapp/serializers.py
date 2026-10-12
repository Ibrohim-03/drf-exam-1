from rest_framework import serializers
from .models import User,Profile,Post,Like,Favorite


class UserSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    favorites_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','age', 'cr_at', 'posts_count','likes_count', 'favorites_count']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user',
        write_only = True
    )

    class Meta:
        model = Profile
        fields = ['user','user_id','bio','city','birth_date','avatar']




class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    favorites_count = serializers.IntegerField(read_only=True)
    is_popular = serializers.SerializerMethodField()

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    def get_is_popular(self, obj):
        return getattr(obj, 'likes_count', 0) >= 10

    class Meta:
        model = Post
        fields = ['id', 'user', 'user_id', 'title', 'content','views', 'cr_at', 'updated_at','likes_count', 'favorites_count', 'is_popular']






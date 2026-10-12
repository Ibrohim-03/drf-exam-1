from rest_framework import serializers
from .models import User,Profile,Post,Like,Favorite


class UserSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    favorites_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','age', 'cr_at', 'posts_count','likes_count', 'favorites_count']




from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .filters import filter_posts
from django.db.models import Count, Sum, Avg, Max, Min
from datetime import timedelta
from django.utils import timezone



@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.annotate(
            posts_count=Count('post'),
            likes_count=Count('like'),
            favorites_count=Count('favorite')
        )
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)












    
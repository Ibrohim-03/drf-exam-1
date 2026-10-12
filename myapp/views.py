from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .filters import filter_posts
from django.db.models import Count, Sum, Avg, Max, Min
from datetime import timedelta
from django.utils import timezone
from drf_yasg.views import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    responses={200: UserSerializer(many=True)}
)

@api_view(['GET'])
def user_statistics(request):
    data = User.objects.aggregate(
        total_users=Count('id'),
        average_age=Avg('age'),
        min_age=Min('age'),
        max_age=Max('age')
    )
    return Response(data)



@swagger_auto_schema(
    method='get',
    responses={200: UserSerializer(many=True)}
)


@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={201: "Created", 400: "Validation error"}
)


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




@swagger_auto_schema(
    method='get',
    responses={200: ProfileSerializer(many=True)}
)


@swagger_auto_schema(
    method='post',
    request_body=ProfileSerializer,
    responses={201: "Created", 400: "Validation error"}
)
@api_view(['GET','POST'])
def profile_list(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)





@swagger_auto_schema(
    method='get',
    responses={200: PostSerializer(many=True)}
)


@swagger_auto_schema(
    method='post',
    request_body=PostSerializer,
    responses={201: "Created", 400: "Validation error"}
)

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.annotate(
            likes_count=Count('like'),
            favorite_count=Count('favorite')

        )
        post = filter_posts(post,request.GET)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)




@swagger_auto_schema(
    method='get',
    responses={200: LikeSerializer(many=True)}
)


@swagger_auto_schema(
    method='post',
    request_body= LikeSerializer,
    responses={201: "Created", 400: "Validation error"}
)

@api_view(['GET','POST'])
def like_list(request):
    if request.method == 'GET':
        like = Like.objects.all()
        serializer = LikeSerializer(like,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

    



@swagger_auto_schema(
    method='get',
    responses={200: FavoriteSerializer(many=True)}
)


@swagger_auto_schema(
    method='post',
    request_body=FavoriteSerializer,
    responses={201: "Created", 400: "Validation error"}
)

@api_view(['GET','POST'])
def favorite_list(request):
    if request.method == 'GET':
        favorite = Favorite.objects.all()
        serializer = FavoriteSerializer(favorite,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)



@swagger_auto_schema(
    method='get',
    responses={200: UserSerializer(many=True)}
)


@swagger_auto_schema(
    method='put',
    request_body=UserSerializer,
    responses={
        200: UserSerializer(),
        204: "Not found",
        400: "Validation error"
    }
)



@api_view(['GET','PUT','DELETE'])
def user_set(request,id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    if request.method=='DELETE':
        user.delete()
        return Response(status=204)



@swagger_auto_schema(
    method='get',
    responses={200: ProfileSerializer(many=True)}
)


@swagger_auto_schema(
    method='put',
    request_body=ProfileSerializer,
    responses={
        200: ProfileSerializer(),
        204: "Not found",
        400: "Validation error"
    }
)


@api_view(['GET','PUT','DELETE'])
def profile_set(request,id):
    try:
        profile = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method=='GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    if request.method=='DELETE':
        profile.delete()
        return Response(status=204)




@swagger_auto_schema(
    method='get',
    responses={200: PostSerializer(many=True)}
)


@swagger_auto_schema(
    method='put',
    request_body=PostSerializer,
    responses={
        200: PostSerializer(),
        204: "Not found",
        400: "Validation error"
    }
)



@api_view(['GET','PUT','DELETE'])
def post_set(request,id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method=='GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    if request.method=='DELETE':
        post.delete()
        return Response(status=204)




@swagger_auto_schema(
    method='get',
    responses={200: LikeSerializer(many=True)}
)



@api_view(['GET','DELETE'])
def like_set(request,id):
    try:
        like = Like.objects.get(pk=id)
    except Like.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method=='GET':
        serializer = LikeSerializer(like)
        return Response(serializer.data)
    if request.method=='DELETE':
        like.delete()
        return Response(status=204)



@swagger_auto_schema(
    method='get',
    responses={200: FavoriteSerializer(many=True)}
)


@swagger_auto_schema(
    method='put',
    request_body=FavoriteSerializer,
    responses={
        200: FavoriteSerializer(),
        204: "Not found",
        400: "Validation error"
    }
)



@api_view(['GET','PUT','DELETE'])
def favorite_set(request,id):
    try:
        favorite = Favorite.objects.get(pk=id)
    except Favorite.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method=='GET':
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = FavoriteSerializer(favorite,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    if request.method=='DELETE':
        favorite.delete()
        return Response(status=204)











    

from django.urls import path
from .views import *

urlpatterns = [
    path('user_statistics/',user_statistics),
    path('users/',user_list),
    path('users/<int:id>/',user_set),
    path('profiles/',profile_list),
    path('profiles/<int:id>/',profile_set),
    path('posts/',post_list),
    path('posts/<int:id>/',post_set),
    path('likes/',like_list),
    path('likes/<int:id>/',like_set),
    path('favorites/',favorite_list),
    path('favorites/<int:id>/',favorite_set),
]
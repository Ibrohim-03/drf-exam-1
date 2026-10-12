
from django.urls import path
from .views import *

urlpatterns = [
    path('user_statistics/',user_statistics),
    path('users/',user_list),
    path('users/<int:id>/',user_set),
    path('profiles/',profile_list),
    path('profiles/<int:id>/'),
    path('posts/',post_list),
    path('posts/<int:id>/',post_set),


]
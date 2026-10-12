
from django.urls import path
from .views import *

urlpatterns = [
    path('user_statistics/',user_statistics),
    path('users/',user_list),
    path('users/<int:id>/',user_set),

]


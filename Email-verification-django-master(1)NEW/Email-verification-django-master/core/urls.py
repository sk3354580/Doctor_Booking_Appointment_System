from django.contrib import admin
from django.urls import path,include
from core.views import *
urlpatterns = [
    path('',home,name='home'),
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('token/',token_send,name='token_send'),
    path('success/',success,name='success'),
    path('verify/<auth_token>/',verify,name='verify'),
    path('error/',error_page,name='error'),
]

#from django.contrib.auth.views import LogoutView
from django.urls import re_path
from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('', views.welcome, name="welcome"),
    re_path('welcome/', views.welcome, name= "welcome"),
    re_path('aboutus/', views.Aboutus),
    re_path('blogs/', views.Blogs, name="blogs"),
    re_path('water/', views.Water, name="water"),
    re_path('health-tips/', views.HealthTips, name='health'),
    re_path('contact/', views.contact, name='contact'),
    re_path('login/', login_view, name="login"),
    re_path('register/', register_user, name="register"),
    re_path("logout/", views.logout, name="logout"),
    re_path("water_ajax", views.water_ajax, name="water_ajax")
]

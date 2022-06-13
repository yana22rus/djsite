from django.urls import path
from django.http import HttpResponse

from admin.views import admin
from main.views import main_site

from .views import *


urlpatterns = [
    path('index/',index,name="index"),
    path("logout",logout,name="logout")
]


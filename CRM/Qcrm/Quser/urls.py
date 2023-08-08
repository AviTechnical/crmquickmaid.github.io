from django.contrib import admin
from django.urls import path, include
from Quser.views import Qlogin

urlpatterns = [
    path("", Qlogin, name='qlogin')
]
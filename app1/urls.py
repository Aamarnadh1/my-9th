from django.urls import path
from app1.views import *
app_name='anushka'
urlpatterns=[
    path('arundhati/',arundhati,name='arundhati'),
]
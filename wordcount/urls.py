from django.urls import path
from .views import *

urlpatterns = [
    path('wordcount', HomePage, name='start'),
    path('wordcount/<int:pk>', WordView, name='word_one')
]
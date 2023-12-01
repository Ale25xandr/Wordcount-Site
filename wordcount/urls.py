from django.urls import path
from .views import *

urlpatterns = [
    path('wordcount', HomePage, name='start'),
    path('wordcount/<int:pk>', WordView, name='word_one'),
    path('wordcount/history/<int:pk>', HistoryView, name='history'),
    path('wordcount/delete/<int:pk>', DeleteHistory, name='delete'),
    path('wordcount//<int:pk>', TemplateDelete, name='del')
]
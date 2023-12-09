# blog/urls.py
from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('<str:room_name>/', views.chat_view, name='chat'),
]

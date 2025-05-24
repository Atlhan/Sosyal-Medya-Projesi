from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("start_chat/<str:username>", views.start_chat, name="start_chat"),
    path("global_chat", views.global_chat, name="global_chat")
]
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Room

def index(request):
    users=User.objects.all().exclude(username=request.user)


    return render(request, "index.html",{"users":users})

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})

def start_chat(request,username):
    second_user=User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user, second_user=second_user)
    except Room.DoesNotExist:
        room = Room.objects.create(first_user=request.user, second_user=second_user)
    return redirect("room", room.id)

def login(request):...

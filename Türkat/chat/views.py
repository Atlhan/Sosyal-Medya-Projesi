from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Room

def index(request):
    users=User.objects.all().exclude(username=request.user)


    return render(request, "kullanıcı.html",{"users":users})

def room(request, room_name):
    users=User.objects.all().exclude(username=request.user)
    room=Room.objects.get(id=room_name)


    return render(request, "oda.html", {"room_name": room_name,"room":room,"users":users})

def start_chat(request,username):
    second_user=User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user, second_user=second_user)   
    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user, first_user=second_user)
        except Room.DoesNotExist:
            room = Room.objects.create(first_user=request.user, second_user=second_user)
    return redirect("room", room.id)

def login(request):...

def global_chat(request):

    return render(request, "globalchat.html")

def post(request):
    posts = Post.objects.all().order.by("date")

    context={
        "posts":posts
    }


    return render(request, "post.html", context)

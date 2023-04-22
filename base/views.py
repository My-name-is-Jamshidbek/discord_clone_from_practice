from django.shortcuts import render
from .models import Room

# Create your views here.


def home(request):
    return render(request, "base/home.html")

def rooms(request):
    rooms_data = Room.objects.all()
    context = {'rooms': rooms_data}

    return render(request, "base/rooms.html", context)

def room(request, pk):
    room_data = Room.objects.get(id=pk)
    context = {'room': room_data}
    return render(request, "base/room.html", context)

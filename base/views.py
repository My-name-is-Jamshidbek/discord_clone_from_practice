from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.


def home(request):
    rooms_data = Room.objects.all()
    context = {'rooms': rooms_data}
    
    return render(request, "base/home.html", context)

def rooms(request):
    rooms_data = Room.objects.all()
    context = {'rooms': rooms_data}

    return render(request, "base/rooms.html", context)

def room(request, pk):
    room_data = Room.objects.get(id=pk)
    context = {'room': room_data}
    
    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {"form": form}
    
    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return  redirect('home')
    context = {'obj': room}
    
    return render(request, "base/room_delete.html", context)

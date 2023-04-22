from django.shortcuts import render

# Create your views here.

rooms_data = [
    {"id": 1, "name": "Anton", "description": "Anton is a project manager for developing"},
    {"id": 2, "name": "Asal", "description": "Asal is a project manager for developing"},
    {"id": 3, "name": "Loran", "description": "Loran is a project manager for developing"}
]

def home(request):
    return render(request, "base/home.html")

def rooms(request):
    context = {'rooms': rooms_data}

    return render(request, "base/rooms.html", context)

def room(request, pk):
    room_data = next(filter(lambda i: i['id'] == pk, rooms_data), None)
    context = {'room': room_data}
    return render(request, "base/room.html", context)

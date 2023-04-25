from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Room, Topic, Message
from .forms import RoomForm
# Create your views here.


def logout(request):
    auth_logout(request)
    return redirect('home')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = auth_authenticate(request = request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Username or password is incorrect")
        
            
            
    context = {}
    return render(request, 'base/login_registration.html', context)


def register(request):
    
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        
    context = {'form': form}
    
    return render(request, 'base/register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ""
    rooms_data = Room.objects.filter(Q(topic__name__icontains = q) |
                                       Q(name__icontains = q) |
                                       Q(description__icontains = q))
    topics_data = Topic.objects.all()
    rooms_count = rooms_data.count()
    messages_data = Message.objects.filter(Q(room__topic__name__icontains=q) |
                                           Q(room__name__icontains = q) |
                                           Q(room__description__icontains = q))
    
    context = {'rooms': rooms_data, 'topics': topics_data, "rooms_count": rooms_count, 'messages_data': messages_data}
    
    return render(request, "base/home.html", context)


def rooms(request):
    rooms_data = Room.objects.all()
    context = {'rooms': rooms_data}

    return render(request, "base/rooms.html", context)


def room(request, pk):
    room_data = Room.objects.get(id=pk)
    messages_data = Message.objects.filter(room__id=room_data.id)
    participants = room_data.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room_data,
            body=request.POST.get('body')
            )
        room_data.participants.add(request.user)
        return redirect('room', pk=room_data.id) 
    context = {'room': room_data, 'messages_data': messages_data, 'participants': participants}
            
    return render(request, "base/room.html", context)


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = Room.objects.filter(participants = user)
    messages_data = Message.objects.filter(user = user)
    topics = Topic.objects.all()
    
    context = {'user': user, 'rooms': rooms, 'messages_data': messages_data, 'topics': topics}
    
    return render(request, 'base/user_profile.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('home')
    context = {"form": form}
    
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)


    if request.user != room.host:
        return HttpResponse("You are not allowed here")    


    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {"form": form}
    
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")    

    if request.method == 'POST':
        room.delete()
        return  redirect('home')
    context = {'obj': room}
    
    return render(request, "base/room_delete.html", context)

@login_required(login_url='login')
def delete_message(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here")    

    if request.method == 'POST':
        message.delete()
        return  redirect('home')
    context = {'obj': message}
    
    return render(request, "base/message_delete.html", context)

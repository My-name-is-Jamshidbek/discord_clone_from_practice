from django.shortcuts import render

# Create your views here.

programmers = [
    {"id": 1, "name": "Anton", "description": "Anton is a project manager for developing"},
    {"id": 2, "name": "Asal", "description": "Asal is a project manager for developing"},
    {"id": 3, "name": "Loran", "description": "Loran is a project manager for developing"}
]

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html", {'programmers': programmers})

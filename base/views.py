from django.shortcuts import render

# Create your views here.

programmers = [
    {"id": 1, "name": "Anton", "description": "Anton is a project manager for developing"},
    {"id": 2, "name": "Asal", "description": "Asal is a project manager for developing"},
    {"id": 3, "name": "Loran", "description": "Loran is a project manager for developing"}
]

def home(request):
    return render(request, "base/home.html")

def abouts(request):
    context = {'programmers': programmers}
    return render(request, "base/abouts.html", context)

def about(request, pk):
    programmer = next(filter(lambda i: i['id'] == pk, programmers), None)
    context = {'programmer': programmer}
    return render(request, "base/about.html", context)

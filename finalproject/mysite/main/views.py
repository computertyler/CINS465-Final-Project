from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Machine, Location
from .import forms

def index(request):
    machines = Machine.objects.all().order_by('game')
    m_list = []
    for m in machines:
        loc = Location.objects.filter(machines=m)
        temp = {}
        temp["game"] = m.game
        temp["manufacturer"] = m.manufacturer
        temp["releaseYear"] = m.releaseYear
        temp["location"] = loc
        m_list += [temp]
    return render(request, "index.html", {'machines': machines, 'm_list': m_list})

def about(request):
    return render(request, "about.html")

def update(request):
    form = forms.addGame()
    return render(request, "update.html", {'form': form})

def test(response):
    return HttpResponse("<h1>Testing 123!</h1>")

def addGame(request):
    if request.method == "POST":
        form = forms.addGame()    
        form = forms.addGame(request.POST)
        if form.is_valid():
            form.save()
            form = forms.addGame()
            return redirect(update)

def addLocation(request):
    if request.method == "POST":
        form = forms.addLocation()    
        form = forms.addLocation(request.POST)
        if form.is_valid():
            form.save()
            form = forms.addLocation()
            return redirect(updateLocation)
        
def updateLocation(request):
    form = forms.addLocation()
    return render(request, "updateLocation.html", {'form': form})

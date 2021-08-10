from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    contexto = {
        "lugares" : ["Farm", "Cave", "House", "Casino"],  
    }

    return render(request, 'app/index.html', contexto)

def procesar(request):
    if request.method == "POST":
        print("a POST request is being made to this route")

        lugar = request.POST["valor"]

        if 'oros' in request.session:
            if lugar == "farm":
                request.session['oros']+=10
            if lugar == "cave":
                request.session['oros']+=5
            if lugar == "house":
                request.session['oros']+=2
            if lugar == "casino":
                request.session['oros'] -=5

        else:
            request.session['oros'] = 0
            if lugar == "farm":
                request.session['oros']+=10
            if lugar == "cave":
                request.session['oros']+=5
            if lugar == "house":
                request.session['oros']+=2
            if lugar == "casino":
                request.session['oros'] -=5
    return redirect("/")


def limpiar(request):
    if request.method == "POST":
        print("a POST request is being made to this route")
    return redirect("/")
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Madre
from .models import Padre
from .models import Hermano

# Create your views here.

def mostrar_familiares(request):
    madre = Madre(nombre = "Patricia", edad = 58, cumpleaños = datetime.date(1964, 8, 11))
    padre = Padre(nombre = "Dario", edad = 60, cumpleaños = datetime.date(1962, 12, 25))
    hermano = Hermano(nombre = "Paulo", edad = 33, cumpleaños = datetime.date(1989, 8, 9))

    return render(request, 'AppFamiliares/familiares.html', {'madre': madre, "padre": padre, "hermano": hermano})


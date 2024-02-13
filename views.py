# 

from django.shortcuts import render
from .models import Articulo
from .forms import ArticuloForm

def home(request):
    articulos = Articulo.objects.all()
    return render(request, 'home.html', {'articulos': articulos})

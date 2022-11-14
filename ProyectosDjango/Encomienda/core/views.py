from django.shortcuts import render
from django.http import HttpResponse
from .models import correspondencia
from django.utils import timezone


#request: realizar peticiones.
#httpResponse: Enviar la respuesta usando el protocola Http.

#Primera view: Home o Bienvenida.
def bienvenida(request):
    posts = correspondencia.objects.all
    return render(request, 'bienvenida.html', {'posts': posts})


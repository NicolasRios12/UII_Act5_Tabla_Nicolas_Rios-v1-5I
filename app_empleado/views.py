from django.shortcuts import render

from .models import Empleado
# Create your views here.
def index(request):

    Empleados = Empleado.objects.all()
    
    return render(request, 'index.html', {'Empleados': Empleados})
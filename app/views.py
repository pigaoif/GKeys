from django.shortcuts import render, redirect
from app.forms import ServidorForm
from app.models import Servidor


# Create your views here.

def home(request):
    return render(request, 'index.html')

def servidor_index(request):
    data = {}
    data['db'] = Servidor.objects.all()
    return render(request, 'servidor_index.html', data)

def servidor_create(request):
    form = ServidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servidor_index')
    
    

def servidor_form(request):
    data = {}
    data['form'] = ServidorForm()
    return render(request, 'servidor_form.html', data)

    


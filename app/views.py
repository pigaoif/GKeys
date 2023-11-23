from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def servidor_index(request):
    return render(request, 'servidor_index.html')

def servidor_create(request):
    return render(request, 'servidor_create.html')

    


from django.shortcuts import render, redirect
from app.forms import ServidorForm
from app.forms import ChaveForm
from app.forms import EmprestimoForm
from app.models import Servidor
from app.models import Chave
from app.models import Emprestimo
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    
    data = {}
    search = request.GET.get('search')
    if search:
        data['emprestimo'] = Emprestimo.objects.filter(id_chave__descricao__icontains=search)
        
    else:    
        data['emprestimo'] = Emprestimo.objects.all()

    return render(request, 'index.html', data)

def servidor_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Servidor.objects.filter(nome__icontains=search)
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Servidor.objects.all()
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'servidor_index.html', {'page': page})

def chave_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Chave.objects.filter(descricao__icontains=search)
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Chave.objects.all()
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'chave_index.html', {'page': page})

def emprestimo_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Emprestimo.objects.filter(data_emprestimo__icontains=search)
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Emprestimo.objects.all()
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'emprestimo_index.html', {'page': page})


def servidor_create(request):
    form = ServidorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('servidor_index')

    return render(request, 'servidor_form.html', {'form': form})

def chave_create(request):
    form = ChaveForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('chave_index')

    return render(request, 'chave_form.html', {'form': form})

def emprestimo_create(request):
    form = EmprestimoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'emprestimo_form.html', {'form': form})

    
def servidor_form(request):
    form = ServidorForm()    
    return render(request, 'servidor_form.html', {'form': form} )

def chave_form(request):
    form = ChaveForm()    
    return render(request, 'chave_form.html', {'form': form} )

def emprestimo_form(request):
    form = EmprestimoForm()    
    return render(request, 'emprestimo_form.html', {'form': form} )


def servidor_view(request, pk):
    data = {}
    data['db'] = Servidor.objects.get(pk=pk)
    
    return render(request, 'servidor_view.html', data)

def chave_view(request, pk):
    data = {}
    data['db'] = Chave.objects.get(pk=pk)
    
    return render(request, 'chave_view.html', data)

def servidor_update(request, pk):   
    data = {}
    data['db'] = Servidor.objects.get(pk=pk)
    form = ServidorForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('servidor_index')

def chave_update(request, pk):   
    data = {}
    data['db'] = Chave.objects.get(pk=pk)
    form = ChaveForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('chave_index')

def servidor_edit(request, pk):
    data = {}
    data['db'] = Servidor.objects.get(pk=pk)
    data['form'] = ServidorForm(instance=data['db']) 
    return render(request, 'servidor_form.html', data)

def chave_edit(request, pk):
    data = {}
    data['db'] = Chave.objects.get(pk=pk)
    data['form'] = ChaveForm(instance=data['db']) 
    return render(request, 'chave_form.html', data)

def servidor_delete(request, pk):
    db = Servidor.objects.get(pk=pk)
    db.delete()    
    return redirect('servidor_index')

def chave_delete(request, pk):
    db = Chave.objects.get(pk=pk)
    db.delete()    
    return redirect('chave_index')
    


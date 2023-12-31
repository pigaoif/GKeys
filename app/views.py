from django.shortcuts import render, redirect
from app.forms import ServidorForm
from app.forms import ChaveForm
from app.forms import EmprestimoForm
from app.forms import DevolucaoForm
from app.models import Servidor
from app.models import Chave
from app.models import Emprestimo
from app.models import Devolucao
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from barcode import EAN13
from django.http import HttpResponse
from django.views.generic import View
from django.utils import timezone
from io import BytesIO
from barcode.writer import ImageWriter 
from PIL import Image, ImageDraw, ImageFont

# Create your views here.


class GerarCodBarraView(View):
    def get(self, request, pk):
        try:
            chave = Chave.objects.get(pk=pk)
            barcode_value = chave.codbarra
            descricao = chave.descricao

            # Cria um objeto BytesIO para armazenar os dados do código de barras
            buffer = BytesIO()

            # Cria o código de barras e salva no buffer
            cod_barra = EAN13(barcode_value, writer=ImageWriter())
            cod_barra.write(buffer)

            # Adicione logs para ajudar a diagnosticar
            print(f"Barcode Value: {barcode_value}")
            print(f"Buffer Size: {buffer.tell()} bytes")

            # Move o ponteiro do buffer de volta para o início
            buffer.seek(0)

            # Configura os cabeçalhos da resposta para forçar o download
            response = HttpResponse(buffer.getvalue(), content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{descricao}_codbarra.png"'

            return response

        except Chave.DoesNotExist:
            return HttpResponse("Chave não encontrada", status=404)


def home(request):  
    data = {}
    search = request.GET.get('search')
    if search:
        data['emprestimo'] = Emprestimo.objects.filter(id_chave__descricao__icontains=search).order_by('data_emprestimo')
        
    else:    
        data['emprestimo'] = Emprestimo.objects.filter(status=True).order_by('data_emprestimo')

    return render(request, 'index.html', data)

def servidor_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Servidor.objects.filter(nome__icontains=search).order_by('nome')
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Servidor.objects.all().order_by('nome')
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'servidor_index.html', {'page': page})

def chave_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Chave.objects.filter(descricao__icontains=search).order_by('descricao')
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Chave.objects.all().order_by('descricao')
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'chave_index.html', {'page': page})

def emprestimo_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Emprestimo.objects.filter(data_emprestimo__icontains=search).order_by('data_emprestimo')
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Emprestimo.objects.all().order_by('data_emprestimo')
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'emprestimo_index.html', {'page': page})

def devolucao_index(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Devolucao.objects.filter(data_devolucao__icontains=search).order_by('data_devolucao')
        paginators = Paginator (data['db'], 1000)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)
    else:    
        data['db'] = Devolucao.objects.all().order_by('data_devolucao')
        paginators = Paginator (data['db'], 10)
        page_num = request.GET.get('page')
        page = paginators.get_page(page_num)

    return render(request, 'devolucao_index.html', {'page': page})


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
            # Obtém a chave associada ao empréstimo
            chave = form.cleaned_data['id_chave']

            # Verifica se a chave está livre
            if chave.status == 'Livre':
                # Salva o empréstimo
                emprestimo = form.save()

                # Atualiza o status da chave para "Emprestada"
                chave.status = 'Emprestada'
                chave.save()

                return redirect('home')
            else:
                # A chave não está livre, informa ao usuário
                form.add_error('id_chave', 'Chave não está livre. Status: ' + chave.status)

    return render(request, 'emprestimo_form.html', {'form': form})

def devolucao_create(request):
    form = DevolucaoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Obtém a chave associada a Devolução
            chave = form.cleaned_data['id_chave']

            
            print(chave.descricao)
            

            # Salva a devolução
            devolucao = form.save()

             # Obtém o empréstimo associado à chave
            emprestimo = get_object_or_404(Emprestimo, id_chave=chave, status=True)

            

            # Atualiza o status do empréstimo para False (devolvido)
            emprestimo.status = False
            emprestimo.save()
          
            # Atualiza o status da chave para "Livre"
            chave.status = 'Livre'
            chave.save()            

            return redirect('home')

    return render(request, 'devolucao_form.html', {'form': form})
  

    
def servidor_form(request):
    form = ServidorForm()    
    return render(request, 'servidor_form.html', {'form': form} )

def chave_form(request):
    form = ChaveForm()    
    return render(request, 'chave_form.html', {'form': form} )

def emprestimo_form(request):
    form = EmprestimoForm()    
    return render(request, 'emprestimo_form.html', {'form': form} )

def devolucao_form(request):
    form = DevolucaoForm()    
    return render(request, 'devolucao_form.html', {'form': form} )


def servidor_view(request, pk):
    data = {}
    data['db'] = Servidor.objects.get(pk=pk)
    
    return render(request, 'servidor_view.html', data)

def chave_view(request, pk):
    data = {}
    data['db'] = Chave.objects.get(pk=pk)
    
    return render(request, 'chave_view.html', data)

def emprestimo_view(request, pk):
    data = {}
    data['db'] = Emprestimo.objects.get(pk=pk)

    return render(request, 'emprestimo_view.html', data)

def devolucao_view(request, pk):
    data = {}
    data['db'] = Devolucao.objects.get(pk=pk)

    return render(request, 'devolucao_view.html', data)

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
    

def get_servidor_by_biometria(request):
    biometria = request.GET.get('biometria', None)
    data = {}

    if biometria:
        try:
            servidor = Servidor.objects.get(biometria=biometria)
            data['id_servidor'] = servidor.pk
            data['nome'] = servidor.nome
        except Servidor.DoesNotExist:
            data['id_servidor'] = None
            data['nome'] = None

    return JsonResponse(data)



def get_chave_by_codbarra(request):
    codbarra = request.GET.get('codbarra', None)
    data = {}

    if codbarra:
        try:
            chave = Chave.objects.get(codbarra=codbarra)
            data['id_chave'] = chave.pk
            data['descricao'] = chave.descricao
            data['status'] = chave.status
        except Chave.DoesNotExist:
            data['id_chave'] = None
            data['descricao'] = None
            data['status'] = None

    return JsonResponse(data)

"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, servidor_index, servidor_create, servidor_form, servidor_view, servidor_update, servidor_edit, servidor_delete
from app.views import chave_index, chave_create, chave_form, chave_view, chave_edit, chave_update, chave_delete,devolucao_view
from app.views import emprestimo_index, emprestimo_create, emprestimo_form, get_servidor_by_biometria, get_chave_by_codbarra,emprestimo_view, devolucao_index, devolucao_create,devolucao_form
from app.views import GerarCodBarraView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('servidor_index/', servidor_index, name='servidor_index'),
    path('chave_index/', chave_index, name='chave_index'),
    path('emprestimo_index/', emprestimo_index, name='emprestimo_index'),
    path('devolucao_index/', devolucao_index, name='devolucao_index'),
    path('servidor_create/', servidor_create, name='servidor_create'),
    path('emprestimo_create/', emprestimo_create, name='emprestimo_create'),
    path('devolucao_create/', devolucao_create, name='devolucao_create'),
    path('chave_create/', chave_create, name='chave_create'),
    path('servidor_form/', servidor_form, name='servidor_form'),
    path('emprestimo_form/', emprestimo_form, name='emprestimo_form'),
    path('devolucao_form/', devolucao_form, name='devolucao_form'),
    path('chave_form/', chave_form, name='chave_form'),
    path('servidor_view/<int:pk>/', servidor_view, name='servidor_view'),
    path('emprestimo_view/<int:pk>/', emprestimo_view, name='emprestimo_view'),
    path('chave_view/<int:pk>/', chave_view, name='chave_view'),
    path('devolucao_view/<int:pk>/', devolucao_view, name='devolucao_view'),
    path('servidor_update/<int:pk>/', servidor_update, name='servidor_update'),
    path('chave_update/<int:pk>/', chave_update, name='chave_update'),
    path('servidor_edit/<int:pk>/', servidor_edit, name='servidor_edit'),
    path('chave_edit/<int:pk>/', chave_edit, name='chave_edit'),
    path('servidor_delete/<int:pk>/', servidor_delete, name='servidor_delete'),
    path('chave_delete/<int:pk>/', chave_delete, name='chave_delete'),
    path('get_servidor_by_biometria/', get_servidor_by_biometria, name='get_servidor_by_biometria'),
    path('get_chave_by_codbarra/', get_chave_by_codbarra, name='get_chave_by_codbarra'),
    path('gerarcodbarra/<int:pk>/', GerarCodBarraView.as_view(), name='gerar_codbarra'),

]


from django import forms
from app.models import Servidor
from app.models import Chave
from app.models import Emprestimo
from app.models import Devolucao
import random




class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = "__all__"

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(ChaveForm, self).__init__(*args, **kwargs)
        # Gera um número aleatório de 12 dígitos para o campo codbarra
        if not self.instance.pk:  # Verifica se é uma nova instância
            self.initial['codbarra'] = ''.join([str(random.randint(0, 9)) for _ in range(12)])

class EmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = Emprestimo
        fields = "__all__"

class DevolucaoForm(forms.ModelForm):
    
    class Meta:
        model = Devolucao
        fields = "__all__"
        
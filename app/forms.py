from django import forms
from .models import Chave
from app.models import Servidor
from app.models import Chave
from app.models import Emprestimo
from app.models import Devolucao
import barcode
from barcode.writer import ImageWriter
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
        
        # Torna o campo codbarra não editável
        self.fields['codbarra'].disabled = True
        self.fields['status'].disabled = True
        
        # Checa se é uma nova instância (ou seja, ainda não salva no banco de dados)
        if not self.instance.pk:
            # Geração do código de barras
            random_digits = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(random_digits, writer=ImageWriter())
            
            # Define o valor inicial do campo codbarra com o código de barras gerado
            self.fields['codbarra'].initial = ean.get_fullcode()
            # Opcional: Caso você queira garantir que o campo seja somente leitura na interface,
            # mesmo após a definição do valor inicial.
            self.fields['codbarra'].widget.attrs['readonly'] = True
   
    
class EmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = Emprestimo
        fields = "__all__"

class DevolucaoForm(forms.ModelForm):
    
    class Meta:
        model = Devolucao
        fields = "__all__"
        
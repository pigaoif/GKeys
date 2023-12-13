from django import forms
from app.models import Servidor
from app.models import Chave
from app.models import Emprestimo



class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = "__all__"

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = "__all__"

class EmprestimoForm(forms.ModelForm):
    
    class Meta:
        model = Emprestimo
        fields = "__all__"
        
from django import forms
from app.models import Servidor
from app.models import Chave


class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = "__all__"

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = "__all__"

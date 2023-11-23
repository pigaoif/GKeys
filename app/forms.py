from django import forms
from app.models import Servidor


class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = "__all__"

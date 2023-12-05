from django.db import models
from django.core.exceptions import ValidationError

CARGO = (
    ('Professor EBTT', 'Professor EBTT'),
    ('Técnico Administrativo', 'Técnico Administrativo'),
    ('Terceirizado', 'Terceirizado'),
    ('Aluno', 'Aluno'),
    ('Visitante', 'Visitante'),
    ('Outro', 'Outro'),
)

class Servidor(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=22, choices=CARGO)
    email = models.EmailField(max_length=150, unique=True)
    biometria = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome
    
    def clean(self):
        # Validação personalizada antes de salvar
        if self.biometria and Servidor.objects.filter(biometria=self.biometria).exclude(pk=self.pk).exists():
            raise ValidationError({'biometria': 'Biometria já existe'})
        
        if self.email and Servidor.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': 'E-mail já existe'})

        # Outras validações...

        super().clean()

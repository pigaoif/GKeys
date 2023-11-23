from django.db import models

# Create your models here.


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
    email = models.CharField(max_length=150, unique=True)
    biometria = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome
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

STATUS = (
    ('Emprestada', 'Emprestada'),
    ('Livre', 'Livre'),
)

class Chave(models.Model):
    descricao = models.CharField(max_length=150)
    status = models.CharField(max_length=22, choices=STATUS, default='Livre')     
    codbarra = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.descricao
        
    
    def clean(self):
        # Validação personalizada antes de salvar
        if self.codbarra and Chave.objects.filter(codbarra=self.codbarra).exclude(pk=self.pk).exists():
            raise ValidationError({'codbarra': 'Código de Barra já existe'})
        
        if self.descricao and Chave.objects.filter(descricao=self.descricao).exclude(pk=self.pk).exists():
            raise ValidationError({'descricao': 'Descrição de chave já está sendo utilizada.'})

        # Outras validações...

        super().clean()

class Emprestimo(models.Model):
    id_servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    id_chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    data_emprestimo = models.DateField(auto_now_add=True) 

    

class Devolucao(models.Model):    
    id_chave = models.ForeignKey(Chave, on_delete=models.CASCADE)    
    data_devolucao = models.DateField(auto_now_add=True) 

    
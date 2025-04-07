from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
import secrets

# Create your models here.
class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Mentorados(models.Model):
    estagio_choices = [
        ('E1', "10-100K"),
        ('E2', '100-1KK'),
    ]
        
 
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    navigator = models.ForeignKey(Navigators, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=16)
    
    def save(self, *args, **kargs):
        if not self.token:
            self.token = self.gerar_token_unico()
        super().save(*args, **kargs)
        
    def gerar_token_unico(self):
        while True:
            token = secrets.token_urlsafe(8)
            if not Mentorados.objects.filter(token=token).exists():
                return token
    
    def __str__(self):
        return self.nome
    
class DisponibilidadeHorarios(models.Model):
    data_inicial = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    agendado = models.BooleanField(default=False)

    @property
    def data_final(self):
        return self.data_inicial + timedelta(minutes=50)
    
class Reuniao(models.Model):
    tag_choices = (
        ('G', 'Gestão'),
        ('M', 'Marketing'),
        ('RH', 'Gestão de pessoas'),
        ('I', 'Impostos')
    )

    data = models.ForeignKey(DisponibilidadeHorarios, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorados, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    descricao = models.TextField()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c87b829 (Iniciando Tarefas)
class Tarefa(models.Model):
    mentorado = models.ForeignKey(Mentorados, on_delete=models.DO_NOTHING)
    tarefa = models.CharField(max_length=255)
    realizada = models.BooleanField(default=False)


class Upload(models.Model):
    mentorado = models.ForeignKey(Mentorados, on_delete=models.DO_NOTHING)
<<<<<<< HEAD
    video = models.FileField(upload_to='video')
=======
>>>>>>> 3d50b9a (Adicionado Reuniões)
=======
    video = models.FileField(upload_to='video')
>>>>>>> c87b829 (Iniciando Tarefas)

from django.db import models

class Usuario(models.Model):
    PERFIS = [
        ('admin', 'Administrador'),
        ('reporter', 'Repórter'),
        ('estagiario', 'Estagiário'),
    ]

    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    perfil = models.CharField(
        max_length=20,
        choices=PERFIS,
        default='estagiario'
    )

    def __str__(self):
        return f"{self.email} ({self.perfil})"


  #  def __str__(self):
   #     return self.email

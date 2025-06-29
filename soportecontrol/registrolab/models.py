from django.db import models

# Create your models here.
class RegistroLab(models.Model):
    carrera = models.EmailField()
    asignatura = models.CharField(max_length=100)
    # horaEntrada = models.TimeField(auto_now_add=True)
    # horaSalida = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.carrera} - {self.asignatura} - {self.docente} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
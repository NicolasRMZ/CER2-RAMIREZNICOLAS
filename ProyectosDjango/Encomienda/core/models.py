from django.db import models

# Create your models here.

class residencia(models.Model):
    idResidencia = models.CharField(max_length=31)
    nombreDueño = models.CharField(max_length=30)
    fonoDueño = models.CharField(max_length=15)
    emailDueño = models.CharField(max_length=30)

class correspondencia (models.Model):
    fechaRecepcion = models.DateTimeField(max_length=10)
    nombreConserje= models.CharField(max_length=30)
    nombreRemitente = models.CharField(max_length=30)
    nombreDestinatario = models.CharField(max_length=30)
    id_Residencia = models.ForeignKey(residencia, on_delete=models.CASCADE)
    Entregado= 'Entregado'
    No_entregado= 'No entregado'
    En_camino= 'En camino'
    ESTADO_CHOICES = [
        (Entregado, 'Entregado'),
        (No_entregado, 'No entregado'),
        (En_camino, 'En camino'),
    ]
    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default=No_entregado,
    )

    def str(self):
        return all

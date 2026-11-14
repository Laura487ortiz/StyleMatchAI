from django.db import models
from django.contrib.auth.models import User

class FotoArmario(models.Model):
    imagen = models.ImageField(upload_to="prendas/")
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fotografía {self.id}"

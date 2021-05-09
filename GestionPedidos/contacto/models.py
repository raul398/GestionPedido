from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    contenido = models.CharField(max_length=50)
    

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.nombre
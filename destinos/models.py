from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=35)
    duracion_dias = models.IntegerField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='destinos/', null=True)

    def __str__(self):
        return self.nombre

    
def delete(self, using=None, keep_parents=False):
    if self.imagen:
        self.imagen.storage.delete(self.imagen.name)
    super().delete(using=using, keep_parents=keep_parents)

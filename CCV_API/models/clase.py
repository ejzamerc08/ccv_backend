from ..models import models

class Clase(models.Model):
    nombre_clase = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
        db_table = 'clase'
        ordering = ['id']

    def __str__(self):
        return f'Clase {self.id}: {self.nombre_clase}'

from ..models import models

class Mision(models.Model):
    nombre_mision = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Mision'
        verbose_name_plural = 'Misiones'
        db_table = 'mision'
        ordering = ['id']

    def __str__(self):
        return f'Mision {self.id}: {self.nombre_mision}'

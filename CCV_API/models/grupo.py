from ..models import models

class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        db_table = 'grupo'
        ordering = ['id']

    def __str__(self):
        return f'Grupo {self.id}: {self.nombre_grupo}'

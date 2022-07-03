from ..models import models, Grupo, Clase, Mision

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=150)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
    clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True)
    mision = models.ForeignKey(Mision, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipo'
        ordering = ['id']

    def __str__(self):
        return f'Equipo {self.id}: {self.nombre_equipo} {self.grupo} {self.clase} {self.mision}'
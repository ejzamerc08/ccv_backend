from ..models import models

class Inflacion(models.Model):
    anio_inflacion = models.IntegerField()
    cpicol = models.FloatField()
    cpiusa = models.FloatField()
    cpieu = models.FloatField()
    cpiuk = models.FloatField()
    cpiyen = models.FloatField()

    class Meta:
        verbose_name = 'Inflacion'
        verbose_name_plural = 'Inflaciones'
        db_table = 'inflacion'
        ordering = ['id']

    def __str__(self):
        return f'Inflacion {self.id}: {self.anio_inflacion} {self.cpicol} {self.cpiusa} {self.cpieu} {self.cpiuk} {self.cpiyen}'

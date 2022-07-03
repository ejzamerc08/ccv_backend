from ..models import models

class TasaCambio(models.Model):
    anio_tasa = models.IntegerField()
    usdcop = models.FloatField()
    usdeur = models.FloatField()
    usdgbp = models.FloatField()
    usdjpy = models.FloatField()
    eurcop = models.FloatField()
    gbpcop = models.FloatField()
    jpycop = models.FloatField()

    class Meta:
        verbose_name = 'Tasa Cambio'
        verbose_name_plural = 'Tasas Cambios'
        db_table = 'tasa_cambio'
        ordering = ['id']

    def __str__(self):
        return f'Tasa Cambio {self.id}: {self.anio_tasa} {self.usdcop} {self.usdeur} {self.usdgbp} {self.usdjpy} {self.eurcop} {self.gbpcop} {self.jpycop}'

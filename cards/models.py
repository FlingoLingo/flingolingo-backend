from django.db import models

# Create your models here.
class Card(models.Model):
    rus = models.CharField(verbose_name='слово на русском', max_length=50)
    eng = models.CharField(verbose_name='слово на английском', max_length=50)
    transcription = models.CharField(verbose_name='транскрипция', max_length=50, blank=True, default='')
    examples = models.CharField(verbose_name='примеры', max_length=500, blank=True, default="")

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return f'{self.pk} {self.rus} {self.eng}'

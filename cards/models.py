from django.db import models

# Create your models here.
class Card(models.Model):
    front = models.CharField(verbose_name='название', max_length=30)
    back = models.CharField(verbose_name='описание', max_length=30)
    examples = models.CharField(verbose_name='примеры', max_length=500, default="")
    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return f'{self.pk} {self.front} {self.back}'

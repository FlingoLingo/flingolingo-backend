from django.db import models
from users.models import User
from cards.models import Card

# Create your models here.
class Deck(models.Model):
    is_private = models.BooleanField(verbose_name='приватная', default=True)
    name = models.CharField(verbose_name='название', max_length=30, default='Новая колода')
    description = models.CharField(verbose_name='описание', max_length=500, default="")
    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, blank=True)
    last_repeated = models.DateTimeField(verbose_name='время последнего повторения', null=True)
    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'

    def __str__(self):
        return f'{self.pk} {self.name}'

class Progress(models.Model):
    is_learned = models.BooleanField(verbose_name='выучена', default=False)
    deck = models.ForeignKey(Deck, verbose_name='колода', related_name='cards',on_delete=models.CASCADE)
    card = models.ForeignKey(Card, verbose_name='карта', related_name='decks', on_delete=models.CASCADE)
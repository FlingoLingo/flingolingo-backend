from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # avatar = models.ImageField(verbose_name='аватар', blank=True)
    # bio = models.CharField(verbose_name='о себе', max_length=500, default="")
    # status = models.CharField(verbose_name='статус', default='не в сети', max_length=20, null=True)
    # birth_date = models.DateField(verbose_name='дата рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.pk} {self.username}'

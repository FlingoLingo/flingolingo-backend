# Generated by Django 4.2 on 2023-04-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_remove_card_back_remove_card_front_card_eng_card_rus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='examples',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='примеры'),
        ),
        migrations.AlterField(
            model_name='card',
            name='transcription',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='транскрипция'),
        ),
    ]

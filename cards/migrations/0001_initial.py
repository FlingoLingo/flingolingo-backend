# Generated by Django 4.2 on 2023-04-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=30, verbose_name='название')),
                ('back', models.CharField(max_length=30, verbose_name='описание')),
                ('examples', models.CharField(default='', max_length=500, verbose_name='примеры')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-04 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_juegos', '0005_juguete_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juguete',
            name='active',
        ),
    ]

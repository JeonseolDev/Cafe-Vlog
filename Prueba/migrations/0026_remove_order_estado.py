# Generated by Django 4.0.3 on 2022-04-09 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0025_rename_nombre2_curso_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='estado',
        ),
    ]

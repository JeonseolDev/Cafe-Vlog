# Generated by Django 4.0.3 on 2022-03-19 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0007_remove_curso_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='data_creada',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0039_rename_ordenes_ordene_remove_usuario_cursada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('En curso', 'En curso')], max_length=200, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-09 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0014_remove_producto_tags_curso_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='producto',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='comprador',
            new_name='usuario',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-09 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0021_rename_usuario2_order_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='nombre2',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-09 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0015_rename_producto_order_curso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Prueba.curso'),
        ),
        migrations.AlterField(
            model_name='order',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Prueba.usuario'),
        ),
    ]

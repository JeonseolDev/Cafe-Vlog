# Generated by Django 4.0.3 on 2022-04-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prueba', '0041_alter_usuario_cursada_alter_usuario_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Prueba.tag'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-20 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
        ('reparaciones', '0002_rename_fecha_reparacion_created_reparacion_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacion',
            name='tenico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.trabajador'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-15 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('computadoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sello_1', models.PositiveIntegerField(default='000000', unique=True)),
                ('sello_2', models.PositiveIntegerField(default='000000', unique=True)),
                ('tenico', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computadoras.computadora')),
            ],
        ),
    ]

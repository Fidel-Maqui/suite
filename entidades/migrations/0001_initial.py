# Generated by Django 4.1.5 on 2023-02-15 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del área', max_length=50, unique=True)),
                ('jefe', models.CharField(blank=True, help_text='Persona responsable del área', max_length=50, null=True, unique=True)),
                ('cant_trabs', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['ueb'],
            },
        ),
        migrations.CreateModel(
            name='Ueb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la UEB', max_length=20, unique=True)),
                ('director', models.CharField(blank=True, help_text='Director de la UEB', max_length=50, null=True, unique=True)),
                ('cant_areas', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('cant_trabs', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del Trabajador', max_length=50, unique=True)),
                ('cargo', models.CharField(help_text='Cargo del Trabajador', max_length=50)),
                ('area', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entidades.area')),
            ],
            options={
                'ordering': ['area'],
            },
        ),
        migrations.AddField(
            model_name='area',
            name='ueb',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='entidades.ueb'),
        ),
    ]

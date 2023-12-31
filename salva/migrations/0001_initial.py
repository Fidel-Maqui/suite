# Generated by Django 4.2.5 on 2023-10-05 15:26

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
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(help_text='Nombre del área', max_length=50, unique=True)),
                ('cant_trabs', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(help_text='Nombre de la computadora', max_length=50, unique=True)),
                ('ip', models.CharField(default='172.19.250.000', max_length=15, unique=True)),
                ('num_de_inventario', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('sello_1', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('sello_2', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('cambios', models.BooleanField(default=False)),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diferencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('computadora', models.CharField(max_length=50)),
                ('campo', models.CharField(max_length=50)),
                ('cambio', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(help_text='Nombre del Trabajador', max_length=50, unique=True)),
                ('cargo', models.CharField(help_text='Cargo del Trabajador', max_length=50)),
                ('jefe', models.BooleanField(default=False)),
                ('director', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='salva.area')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.computadora')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.programs')),
            ],
        ),
        migrations.CreateModel(
            name='Periferico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(choices=[('Monitor', 'Monitor'), ('Teclado', 'Teclado'), ('Ups', 'Ups'), ('Mouse', 'Mouse')], default='Monitor', max_length=7)),
                ('fabricante', models.CharField(blank=True, help_text='Fabricante del periférico', max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, help_text='Módelo del periférico', max_length=50, null=True, verbose_name='módelo')),
                ('num_inventario', models.CharField(blank=True, default='200000', max_length=50, null=True)),
                ('num_de_serie', models.CharField(blank=True, help_text='No. de serie', max_length=50, null=True)),
                ('baja', models.BooleanField(default=0)),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.computadora')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(choices=[('CPU', 'CPU'), ('RAM', 'RAM'), ('BOARD', 'BOARD'), ('DISCO', 'DISCO'), ('CD-ROM', 'CD-ROM')], default='CPU', max_length=14)),
                ('fabricante', models.CharField(blank=True, help_text='Fabricante de la pieza', max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, help_text='Módelo de la pieza', max_length=50, null=True, verbose_name='módelo')),
                ('capacidad_gb', models.CharField(blank=True, help_text='Cantidad', max_length=50, null=True, verbose_name='Capacidad')),
                ('velocidad', models.CharField(blank=True, help_text='Velocidad', max_length=50, null=True)),
                ('num_de_serie', models.CharField(blank=True, help_text='No. de serie', max_length=50, null=True)),
                ('baja', models.BooleanField(default=0)),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.computadora')),
            ],
        ),
        migrations.AddField(
            model_name='computadora',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salva.trabajador'),
        ),
    ]

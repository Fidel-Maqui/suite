# Generated by Django 4.2.5 on 2023-10-05 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salva', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='computadora',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='diferencias',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='periferico',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='programs',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='softwares',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='pid',
        ),
    ]
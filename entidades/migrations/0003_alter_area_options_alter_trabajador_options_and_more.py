# Generated by Django 4.2.5 on 2023-10-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_alter_area_ueb_alter_trabajador_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='trabajador',
            options={'ordering': ['nombre']},
        ),
        migrations.RemoveField(
            model_name='area',
            name='jefe',
        ),
        migrations.RemoveField(
            model_name='area',
            name='ueb',
        ),
        migrations.AddField(
            model_name='trabajador',
            name='director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='jefe',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Ueb',
        ),
    ]
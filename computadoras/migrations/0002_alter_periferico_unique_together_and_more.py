# Generated by Django 4.1.5 on 2023-02-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='periferico',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='periferico',
            name='num_de_serie',
            field=models.CharField(blank=True, help_text='No. de serie', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='periferico',
            name='num_inventario',
            field=models.CharField(blank=True, default='200000', max_length=50, null=True),
        ),
    ]

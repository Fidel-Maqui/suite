# Generated by Django 4.1.5 on 2023-04-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdfConf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=200)),
                ('empresa', models.CharField(max_length=50)),
                ('aprobador', models.CharField(max_length=50)),
                ('responsable_seg', models.CharField(max_length=50)),
                ('responsable_tec', models.CharField(max_length=50)),
            ],
        ),
    ]

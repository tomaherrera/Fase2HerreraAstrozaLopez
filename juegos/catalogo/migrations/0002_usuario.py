# Generated by Django 3.1.2 on 2020-11-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(help_text='Ingrese rut sin dígito verificador.', max_length=8, primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=20)),
            ],
        ),
    ]
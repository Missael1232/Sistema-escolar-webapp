# Generated by Django 5.0.2 on 2025-05-18 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0004_eventos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='lugar',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='programa',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='publico',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='responsable',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='tipo',
        ),
    ]

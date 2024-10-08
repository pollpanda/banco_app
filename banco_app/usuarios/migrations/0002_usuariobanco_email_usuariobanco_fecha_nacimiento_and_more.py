# Generated by Django 5.1.1 on 2024-09-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariobanco',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuariobanco',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuariobanco',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usuariobanco',
            name='tipo_documento',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte')], max_length=2),
        ),
    ]

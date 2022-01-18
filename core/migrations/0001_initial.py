# Generated by Django 3.2.8 on 2021-10-14 00:18

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la pausa activa')),
                ('icon_svg', models.FileField(upload_to='active-pauses/icons/', verbose_name='Icono en SVG')),
                ('number_of_exercises', models.IntegerField(default=0, verbose_name='Número de ejercicios')),
                ('duration', models.CharField(max_length=10, verbose_name='Duración')),
            ],
            options={
                'verbose_name': 'Pausa Activa',
                'verbose_name_plural': 'Pausas Activas',
            },
        ),
        migrations.CreateModel(
            name='Prevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la prevención')),
                ('active_pause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.activepause', verbose_name='Pausa activa')),
            ],
            options={
                'verbose_name': 'Que previene',
                'verbose_name_plural': 'Que previene',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la empresa')),
                ('logo', models.ImageField(upload_to='company/logos/', verbose_name='Logo de la empresa')),
                ('mascot', models.FileField(upload_to='company/mascots/', verbose_name='Mascota de la empresa')),
                ('primary_color', colorfield.fields.ColorField(default='#4a5bb2', max_length=18, verbose_name='Color primario de la empresa')),
                ('secondary_color', colorfield.fields.ColorField(default='#a48421', max_length=18, verbose_name='Color secundario de la empresa')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario dueño')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la actividad')),
                ('active_pause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.activepause', verbose_name='Pausa activa')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.AddField(
            model_name='activepause',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company', verbose_name='Empresa'),
        ),
    ]

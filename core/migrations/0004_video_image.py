# Generated by Django 3.2.8 on 2022-01-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_activepause_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='active-pauses/videos/images/', verbose_name='Imágen'),
        ),
    ]

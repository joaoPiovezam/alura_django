# Generated by Django 4.2.6 on 2023-10-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/fotos/%Y/%m/%d'),
        ),
    ]

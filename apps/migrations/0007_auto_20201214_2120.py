# Generated by Django 3.1.3 on 2020-12-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20201212_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='altsayfa',
            name='dosya',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='duyuru',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
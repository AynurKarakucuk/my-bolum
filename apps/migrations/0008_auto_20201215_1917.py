# Generated by Django 3.1.3 on 2020-12-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20201214_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='resim',
        ),
        migrations.AddField(
            model_name='banner',
            name='alan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='baslik',
            field=models.CharField(max_length=100),
        ),
    ]

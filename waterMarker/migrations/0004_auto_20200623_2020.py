# Generated by Django 3.0.7 on 2020-06-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterMarker', '0003_auto_20200622_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='path',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='position',
            field=models.CharField(default='bcl', max_length=3),
        ),
    ]

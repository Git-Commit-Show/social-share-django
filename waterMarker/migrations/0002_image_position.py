# Generated by Django 3.0.7 on 2020-06-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterMarker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.CharField(default='tl', max_length=3),
        ),
    ]
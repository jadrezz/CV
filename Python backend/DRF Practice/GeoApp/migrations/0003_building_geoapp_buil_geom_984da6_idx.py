# Generated by Django 5.0.6 on 2024-07-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoApp', '0002_auto_20240702_0841'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='building',
            index=models.Index(fields=['geom'], name='GeoApp_buil_geom_984da6_idx'),
        ),
    ]

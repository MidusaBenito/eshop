# Generated by Django 3.1.5 on 2021-01-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210110_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]

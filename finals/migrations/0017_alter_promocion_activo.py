# Generated by Django 4.2.6 on 2023-12-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finals', '0016_promocion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

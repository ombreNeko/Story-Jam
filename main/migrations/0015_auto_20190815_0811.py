# Generated by Django 2.2.4 on 2019-08-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190815_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.IntegerField(choices=[(1, 'dystopia'), (2, 'scifi'), (3, 'romance'), (4, 'fantasy'), (5, 'horror')]),
        ),
    ]

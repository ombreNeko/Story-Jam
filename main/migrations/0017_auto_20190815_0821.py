# Generated by Django 2.2.4 on 2019-08-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190815_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('dystopia', 'dystopia'), ('scifi', 'scifi'), ('romance', 'romance'), ('horror', 'horror')], max_length=256),
        ),
    ]

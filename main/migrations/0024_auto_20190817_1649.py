# Generated by Django 2.2.4 on 2019-08-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20190816_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producerprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='upload_dp/'),
        ),
        migrations.AlterField(
            model_name='writerprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='upload_dp/'),
        ),
    ]

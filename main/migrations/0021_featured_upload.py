# Generated by Django 2.2.4 on 2019-08-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20190815_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='upload_featured/'),
        ),
    ]
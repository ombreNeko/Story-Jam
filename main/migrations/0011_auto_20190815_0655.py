# Generated by Django 2.2.4 on 2019-08-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_story_producer'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='upload_story/'),
        ),
        migrations.AddField(
            model_name='story',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-11 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190811_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='story',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Story'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-11 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190811_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.ProducerProfile'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Story'),
        ),
    ]

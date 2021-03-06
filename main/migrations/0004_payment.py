# Generated by Django 2.2.4 on 2019-08-11 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_genre_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('cc', 'Credit Card'), ('dc', 'Debit Card')], max_length=256)),
                ('payment_time', models.DateTimeField(auto_now_add=True)),
                ('card_number', models.CharField(max_length=256)),
                ('card_cvv', models.CharField(max_length=3)),
                ('card_exp', models.CharField(max_length=5)),
                ('name_on_card', models.CharField(max_length=256)),
                ('producer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.ProducerProfile')),
                ('story', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Story')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-04-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_type', models.CharField(default='None', max_length=100)),
                ('transportation', models.CharField(default='None', max_length=100)),
                ('accommodation', models.CharField(default='None', max_length=100)),
                ('outdoor_adventures', models.CharField(default='None', max_length=100)),
                ('cultural_experiences', models.CharField(default='None', max_length=100)),
                ('specific_cuisine', models.CharField(default='None', max_length=100)),
                ('plan', models.CharField(default='None', max_length=2000)),
                ('question', models.CharField(default='None', max_length=2000)),
            ],
        ),
    ]

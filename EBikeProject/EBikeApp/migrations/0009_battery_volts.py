# Generated by Django 4.0.4 on 2022-04-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBikeApp', '0008_alter_battery_watthour_alter_battery_lifetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='battery',
            name='volts',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBikeApp', '0002_alter_user_userid_alter_user_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserId',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-07 10:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 10, 27, 29, 383160, tzinfo=utc)),
        ),
    ]

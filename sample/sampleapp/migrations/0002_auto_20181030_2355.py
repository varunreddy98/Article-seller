# Generated by Django 2.1.2 on 2018-10-30 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 30, 18, 25, 16, 302798, tzinfo=utc)),
        ),
    ]
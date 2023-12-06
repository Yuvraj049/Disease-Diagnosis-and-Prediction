# Generated by Django 4.1.5 on 2023-11-10 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_report_date_report_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='time',
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

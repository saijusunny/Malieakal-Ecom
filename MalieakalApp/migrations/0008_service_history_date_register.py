# Generated by Django 4.0.2 on 2023-11-08 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0007_service_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_history',
            name='date_register',
            field=models.DateField(default=datetime.date(2023, 11, 8)),
        ),
    ]

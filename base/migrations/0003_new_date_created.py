# Generated by Django 4.2.3 on 2023-09-25 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="new",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 9, 25, 5, 47, 42, 842926, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
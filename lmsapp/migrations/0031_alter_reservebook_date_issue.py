# Generated by Django 4.0.6 on 2022-07-22 20:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0030_alter_reservebook_date_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservebook',
            name='date_issue',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 20, 28, 20, 274187, tzinfo=utc), null=True),
        ),
    ]

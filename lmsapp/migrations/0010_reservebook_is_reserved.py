# Generated by Django 4.0.6 on 2022-07-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0009_remove_user_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservebook',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0006_alter_issuebook_date_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='date_return',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

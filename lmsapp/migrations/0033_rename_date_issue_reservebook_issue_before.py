# Generated by Django 4.0.6 on 2022-07-22 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0032_alter_reservebook_date_issue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservebook',
            old_name='date_issue',
            new_name='issue_before',
        ),
    ]

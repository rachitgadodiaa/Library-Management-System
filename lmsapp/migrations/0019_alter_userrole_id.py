# Generated by Django 4.0.6 on 2022-07-21 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0018_remove_userrole_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_fk', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
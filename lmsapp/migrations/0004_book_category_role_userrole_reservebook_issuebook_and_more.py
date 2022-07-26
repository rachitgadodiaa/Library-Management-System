# Generated by Django 4.0.6 on 2022-07-20 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
            ],
            options={
                'unique_together': {('title', 'author')},
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('date_reserved', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
                ('role_name', models.ForeignKey(db_column='role_name', on_delete=django.db.models.deletion.CASCADE, related_name='book_fk', to='lmsapp.role', to_field='name')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReserveBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('date_reserved', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservebook_book_fk', to='lmsapp.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservebook_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('date_return', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuebook_book_fk', to='lmsapp.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuebook_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_deleted', models.DateTimeField(null=True)),
                ('date_reserved', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateTimeField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookcategory_bookfk', to='lmsapp.book')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookcategory_categoryfk', to='lmsapp.category')),
            ],
        ),
    ]

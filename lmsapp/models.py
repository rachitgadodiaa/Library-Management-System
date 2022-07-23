import datetime

from django.contrib.auth.models import UserManager

from django.contrib.auth.models import AbstractUser
from django.db import models
# from timestamps.models import models, Model
# from safedelete.models import SafeDeleteModel
# from safedelete.models import HARD_DELETE_NOCASCADE
# Create your models here.
from django.utils import timezone


# class Timestampable(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract = True
#
#
# class SoftDeletes(models.Model):
#     deleted_at = models.DateTimeField(null=True)

class User(AbstractUser):
    # _safedelete_policy = HARD_DELETE_NOCASCADE

    first_name = models.CharField(max_length=301)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    password = models.CharField(max_length=100, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    REQUIRED_FIELDS = []


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    is_reserved = models.BooleanField(default=False)
    is_issued = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'author',)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)




class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)


class IssueBook(models.Model):
    user_id = models.ForeignKey(User, related_name='issuebook_user_fk', on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, related_name='issuebook_book_fk', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    fine = models.PositiveIntegerField(null=True)
    # class Meta:
    #     unique_together = ('user_id', 'book_id')


class ReserveBook(models.Model):
    user_id = models.ForeignKey(User, related_name='reservebook_user_fk', on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, related_name='reservebook_book_fk', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    date_reserved = models.DateTimeField(auto_now_add=True)
    issue_before = models.DateTimeField(null=False)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)

    # is_reserved = models.BooleanField(default=False)
    # class Meta:
    #     unique_together = ('user_id', 'book_id')


class BookCategory(models.Model):
    book_id = models.ForeignKey(Book, related_name='bookcategory_bookfk', on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, to_field='name', db_column='category_name', related_name='bookcategory_categoryfk', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    date_reserved = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)

    class Meta:
        unique_together = ('book_id', 'category_name')


class UserRole(models.Model):
    id = models.OneToOneField(User, related_name='user_fk', on_delete=models.CASCADE, primary_key=True)
    # user_name = models.ForeignKey(User, to_field='username', db_column='username', related_name='username_fk', on_delete=models.CASCADE)
    role_name = models.ForeignKey(Role, to_field='name', db_column='role_name', related_name='book_fk', default='Student', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_deleted = models.DateTimeField(null=True)
    date_reserved = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=False)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)


    class Meta:
        unique_together = ('id', 'role_name')



    # class Meta:
    #     db_table = 'lmsapp_user'
    # def save(self):
    #     if self.id:
    #         self.date_updated = datetime.now()
    #     else:
    #         self.date_created = datetime.now()
    #     super(User, self).save()

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.date_created = timezone.now()
    #     if self.id:
    #         self.date_updated = timezone.now()
    #     return super(User, self).save(*args, **kwargs)

# class SoftDeleteModel(models.Model):
#     is_deleted = models.BooleanField(default=False)
#
#     def soft_delete(self):
#         self.is_deleted = True
#         self.save()
#
#     def restore(self):
#         self.is_deleted = False
#         self.save()
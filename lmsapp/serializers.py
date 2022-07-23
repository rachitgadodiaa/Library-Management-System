from rest_framework import serializers
from .models import *
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'username', 'password'
        )
        # exclude = (
        #     'first_name',
        # )

    def validate(self, args):
        email = args.get('email')
        username = args.get('username')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Username already exists.'})
        return super().validate(args)
    #


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'deleted_by', 'date_deleted'
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'title', 'author', 'description'
        )


class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id', 'deleted_by'
        )


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id', 'name'
        )


class RoleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id', 'deleted_by', 'date_deleted'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name'
        )


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'deleted_by', 'date_deleted'
        )


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = (
            'id', 'user_id', 'book_id'
        )


class IssueBookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = (
            'id', 'deleted_by'
        )


class ReserveBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveBook
        fields = (
            'id', 'user_id', 'book_id'
        )


class ReserveBookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveBook
        fields = (
            'id', 'deleted_by', 'date_deleted'
        )


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = (
            'id', 'book_id', 'category_id'
        )


class BookCategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = (
            'id', 'deleted_by'
        )


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = (
            'id', 'role_name'
        )


class UserRoleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = (
            'id', 'deleted_by', 'date_deleted'
        )


class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = (
            'id', 'updated_by'
        )


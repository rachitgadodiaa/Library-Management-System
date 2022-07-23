from datetime import timedelta

from django.shortcuts import render
import psycopg2
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lmsapp.models import *
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
# from django.contrib.auth.models import User
from .serializers import *
from django.utils import timezone
from rest_framework import permissions
from .permissions import AdminPermission


# Create your views here.

class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user_obj = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            username=request.data['username'],
            password=request.data['password']
        )
        request_user_id = User.objects.get(username=request.data['username']).id
        user_role_obj = UserRole.objects.create(
            id_id=request_user_id,
            role_name_id='Student',
            created_by=request_user_id
        )
        # user_obj.save()
        result = UserSerializer(instance=user_obj).data
        return Response(data=result)




class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(deleted_by=None)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_role_obj = UserRole.objects.get(pk=request.user.id)
        user_obj = User.objects.get(pk=kwargs['pk'])
        user_obj.save()
        if request.user.id == kwargs['pk'] or user_role_obj.role_name.name == 'Admin':
            obj = User.objects.get(pk=kwargs['pk'])
            result = UserSerializer(instance=obj).data
            return Response(data=result)
            # serializer = self.get_serializer(instance=user_obj, data=request.data)
            # if serializer.is_valid():
            #     return Response(serializer.data)
            # else:
            #     return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error, User does not have permission to view this profile")

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = User.objects.get(pk=kwargs['pk'])
        user_role_obj = UserRole.objects.get(pk=request.user.id)
        if request.user.id == kwargs['pk'] or user_role_obj.role_name.name == 'Admin':
            obj.updated_by = request.user.id
            obj.date_updated = timezone.now()
            obj.save()
            if request.method == 'PATCH':
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            if request.method == 'PUT':
                partial = kwargs.pop('partial', False)
                instance = self.get_object()
                serializer = self.get_serializer(instance=instance, data=data, partial=partial)
                if serializer.is_valid():
                    for i in range(0, len(data)):
                        setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                        obj.save()
                else:
                    return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error, user does not have permission to edit this profile")
        result = UserSerializer(instance=obj).data
        return Response(data=result)

    # print(list(data.items()))
    # print(list(data.items())[0][0])

    # UserSerializer(obj, data=data, partial=False)
    # return Response(request.data)

    #     user_obj = User.objects.get(pk=kwargs['pk'])
    #     user_obj.save()
    #     result = UserSerializer(instance=user_obj).data
    #     return Response(data=result)
    # return Response("Error")


class UserList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = User.objects.filter(deleted_by=None)
    serializer_class = UserSerializer


class UserDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer

    # def update(self, request, *args, **kwargs):

    def patch(self, request, *args, **kwargs):
        user_obj = User.objects.get(pk=kwargs['pk'])
        data = request.data
        user_obj.updated_by = request.user.id
        user_obj.deleted_by = request.user.id
        user_obj.date_updated = timezone.now()
        user_obj.date_deleted = timezone.now()
        user_obj.save()
        result = UserDeleteSerializer(instance=user_obj).data
        return Response(data=result)

        # super(self.queryset, self).update(date_deleted=timezone.now())


class BookRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = BookSerializer

    def post(self, request):
        obj = Book.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            author=request.data['author'],
            created_by=request.user.id
        )

        # obj.save()
        result = BookSerializer(instance=obj).data
        return Response(data=result)


class BookRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Book.objects.filter(deleted_by=None)
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = Book.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = BookSerializer(instance=obj).data
        return Response(data=result)


class BookList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AdminPermission]
    queryset = Book.objects.filter(deleted_by=None)
    serializer_class = BookSerializer


class BookDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def patch(self, request, *args, **kwargs):
        book_obj = Book.objects.get(pk=kwargs['pk'])
        data = request.data
        book_obj.updated_by = request.book.id
        book_obj.deleted_by = request.book.id
        book_obj.date_updated = timezone.now()
        book_obj.date_deleted = timezone.now()
        book_obj.save()
        result = BookDeleteSerializer(instance=book_obj).data
        return Response(data=result)


class RoleRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = RoleSerializer

    def post(self, request):
        obj = Role.objects.create(
            name=request.data['name'],
            created_by=request.user.id
        )
        # obj.save()
        result = RoleSerializer(instance=obj).data
        return Response(data=result)


class RoleRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Role.objects.filter(deleted_by=None)
    serializer_class = RoleSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = Role.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = RoleSerializer(instance=obj).data
        return Response(data=result)


class RoleList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = Role.objects.filter(deleted_by=None)
    serializer_class = RoleSerializer


class RoleDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def patch(self, request, *args, **kwargs):
        role_obj = Role.objects.get(pk=kwargs['pk'])
        data = request.data
        role_obj.updated_by = request.role.id
        role_obj.deleted_by = request.role.id
        role_obj.date_updated = timezone.now()
        role_obj.date_deleted = timezone.now()
        role_obj.save()
        result = RoleDeleteSerializer(instance=role_obj).data
        return Response(data=result)


class CategoryRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = CategorySerializer

    def post(self, request):
        obj = Category.objects.create(
            name=request.data['name'],
            created_by=request.user.id
        )
        # obj.save()
        result = CategorySerializer(instance=obj).data
        return Response(data=result)


class CategoryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Category.objects.filter(deleted_by=None)
    serializer_class = CategorySerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = Category.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = CategorySerializer(instance=obj).data
        return Response(data=result)


class CategoryList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = Category.objects.filter(deleted_by=None)
    serializer_class = CategorySerializer


class CategoryDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def patch(self, request, *args, **kwargs):
        category_obj = Category.objects.get(pk=kwargs['pk'])
        data = request.data
        category_obj.updated_by = request.category.id
        category_obj.deleted_by = request.category.id
        category_obj.date_updated = timezone.now()
        category_obj.date_deleted = timezone.now()
        category_obj.save()
        result = CategoryDeleteSerializer(instance=category_obj).data
        return Response(data=result)


class IssueBookRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = IssueBookSerializer

    def post(self, request):
        book_obj = Book.objects.get(pk=request.data['book_id'])
        res_book_obj = ReserveBook.objects.filter(book_id=request.data['book_id']).last()
        delta = 0
        if res_book_obj is not None:
            delta = timezone.now().day - res_book_obj.issue_before.day
        if delta > 0:
            book_obj.is_reserved = False
            book_obj.save()
        if book_obj.is_reserved is True and request.data['user_id'] == res_book_obj.user_id_id:
            book_obj.is_reserved = False
            book_obj.save()
        elif book_obj.is_reserved is True and request.data['user_id'] != res_book_obj.user_id_id:
            return Response("This book is issued/reserved by some other user")
            # BookSerializer(instance=book_obj)
        if book_obj.is_issued is False and book_obj.is_reserved is False:
            obj = IssueBook.objects.create(
                user_id_id=User.objects.get(pk=request.data['user_id']).id,
                book_id_id=Book.objects.get(pk=request.data['book_id']).id,
                created_by=request.user.id,
                return_date=timezone.now()+timedelta(days=14)
            )
            book_obj = Book.objects.get(pk=request.data['book_id'])
            book_obj.is_issued = True
            book_obj.date_updated = timezone.now()
            book_obj.updated_by = request.user.id
            book_obj.save()
            BookSerializer(instance=book_obj)
                    # obj.save()
            result = IssueBookSerializer(instance=obj).data
            return Response(data=result)
        return Response('Error.')


class IssueBookRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = IssueBook.objects.filter(deleted_by=None)
    serializer_class = IssueBookSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = IssueBook.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = IssueBookSerializer(instance=obj).data
        return Response(data=result)


class IssueBookList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = IssueBook.objects.filter(deleted_by=None)
    serializer_class = IssueBookSerializer


class IssueBookDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer

    def patch(self, request, *args, **kwargs):
        issue_book_obj = IssueBook.objects.get(pk=kwargs['pk'])
        data = request.data
        issue_book_obj.updated_by = request.issue_book.id
        issue_book_obj.deleted_by = request.issue_book.id
        issue_book_obj.date_updated = timezone.now()
        issue_book_obj.date_deleted = timezone.now()
        issue_book_obj.save()
        result = IssueBookDeleteSerializer(instance=issue_book_obj).data
        return Response(data=result)


class ReserveBookRegistration(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReserveBookSerializer

    def post(self, request):
        book_obj = Book.objects.get(pk=request.data['book_id'])
        res_book_obj = ReserveBook.objects.filter(book_id=request.data['book_id']).last()
        # print(res_book_obj)
        if res_book_obj is not None:
            delta = timezone.now() - res_book_obj.issue_before
            if delta.days > 0:
                book_obj.is_reserved = False
        if book_obj.is_issued is False and book_obj.is_reserved is False:
            obj = ReserveBook.objects.create(
                user_id_id=request.user.id,
                book_id_id=book_obj.id,
                created_by=request.user.id,
                issue_before=timezone.now()+timedelta(days=2)
            )
            book_obj = Book.objects.get(pk=request.data['book_id'])
            book_obj.is_reserved = True
            book_obj.save()
            BookSerializer(instance=book_obj)
        # obj.save()
            result = ReserveBookSerializer(instance=obj).data
            return Response(data=result)
        return Response('Book is already issued or reserved')


class ReserveBookRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = ReserveBook.objects.filter(deleted_by=None)
    serializer_class = ReserveBookSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = ReserveBook.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = ReserveBookSerializer(instance=obj).data
        return Response(data=result)


class ReserveBookList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = ReserveBook.objects.filter(deleted_by=None)
    serializer_class = ReserveBookSerializer


class ReserveBookDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = ReserveBook.objects.all()
    serializer_class = ReserveBookSerializer

    def patch(self, request, *args, **kwargs):
        reserve_book_obj = ReserveBook.objects.get(pk=kwargs['pk'])
        data = request.data
        reserve_book_obj.updated_by = request.reserve_book.id
        reserve_book_obj.deleted_by = request.reserve_book.id
        reserve_book_obj.date_updated = timezone.now()
        reserve_book_obj.date_deleted = timezone.now()
        reserve_book_obj.save()
        result = ReserveBookDeleteSerializer(instance=reserve_book_obj).data
        return Response(data=result)


class BookCategoryRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = BookCategorySerializer

    def post(self, request):
        obj = BookCategory.objects.create(
            book_id_id=request.data['book_id'],
            category_id_id=request.data['category_id'],
            created_by=request.user.id
        )
        # obj.save()
        result = BookCategorySerializer(instance=obj).data
        return Response(data=result)


class BookCategoryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = BookCategory.objects.filter(deleted_by=None)
    serializer_class = BookCategorySerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = BookCategory.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = BookCategorySerializer(instance=obj).data
        return Response(data=result)


class BookCategoryList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = BookCategory.objects.filter(deleted_by=None)
    serializer_class = BookCategorySerializer


class BookCategoryDelete(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

    def patch(self, request, *args, **kwargs):
        book_category_obj = BookCategory.objects.get(pk=kwargs['pk'])
        data = request.data
        book_category_obj.updated_by = request.user.id
        book_category_obj.deleted_by = request.user.id
        book_category_obj.date_updated = timezone.now()
        book_category_obj.date_deleted = timezone.now()
        book_category_obj.save()
        result = BookCategoryDeleteSerializer(instance=book_category_obj).data
        return Response(data=result)


class UserRoleRegistration(generics.CreateAPIView):
    permission_classes = [AdminPermission]
    serializer_class = UserRoleSerializer

    def post(self, request):
        obj = UserRole.objects.create(
            id_id=request.data['id'],
            role_name_id=request.data['role_name'],
            created_by=request.user.id
        )
        result = UserRoleSerializer(instance=obj).data
        return Response(data=result)


class UserRoleRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = UserRole.objects.filter(deleted_by=None)
    serializer_class = UserRoleSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        obj = UserRole.objects.get(pk=kwargs['pk'])
        obj.updated_by = request.user.id
        obj.date_updated = timezone.now()
        obj.save()
        if request.method == 'PATCH':
            for i in range(0, len(data)):
                setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                obj.save()
        if request.method == 'PUT':
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance=instance, data=data, partial=partial)
            if serializer.is_valid():
                for i in range(0, len(data)):
                    setattr(obj, list(data.items())[i][0], list(data.items())[i][1])
                    obj.save()
            else:
                return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        result = UserRoleSerializer(instance=obj).data
        return Response(data=result)


class UserRoleList(generics.ListAPIView):
    permission_classes = [AdminPermission]
    # permission_classes = [AdminPermission]
    queryset = UserRole.objects.filter(deleted_by=None)
    serializer_class = UserRoleSerializer


class UserRoleDelete(generics.DestroyAPIView):
    permission_classes = [AdminPermission]
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

    def patch(self, request, *args, **kwargs):
        user_role_obj = UserRole.objects.get(pk=kwargs['pk'])
        data = request.data
        user_role_obj.updated_by = request.user.id
        user_role_obj.deleted_by = request.user.id
        user_role_obj.date_updated = timezone.now()
        user_role_obj.date_deleted = timezone.now()
        user_role_obj.save()
        result = UserRoleDeleteSerializer(instance=user_role_obj).data
        return Response(data=result)


class ReturnBook(generics.UpdateAPIView):
    permission_classes = [AdminPermission]
    queryset = IssueBook.objects.all()
    serializer_class = ReturnBookSerializer

    def post(self, request, *args, **kwargs):
        book_obj = Book.objects.get(pk=kwargs['pk'])

        if book_obj.is_issued is True:

            # obj.save()
            return_book_obj = IssueBook.objects.filter(book_id=kwargs['pk']).last()

            print(return_book_obj)
            return_book_obj.date_returned = timezone.now()
            delta = return_book_obj.date_returned - return_book_obj.date_issued
            if delta.days > 14:
                return_book_obj.fine = delta.days * 5
            return_book_obj.date_updated = timezone.now()
            return_book_obj.save()
            result = IssueBookDeleteSerializer(instance=return_book_obj).data

            book_obj.is_issued = False
            book_obj.updated_by = request.user.id
            book_obj.date_updated = timezone.now()
            book_obj.save()
            BookSerializer(instance=book_obj)
            return Response(data=result)
            # result = IssueBookSerializer(instance=book_obj).data
            # return Response(data=result)
        return Response('Book is already issued or reserved')




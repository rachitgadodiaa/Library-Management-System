from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from lmsapp.views import *
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('user/create', UserRegistration.as_view()),
    path('user/update/<int:pk>', UserRetrieveUpdate.as_view()),
    path('user/list', UserList.as_view()),
    path('user/delete/<int:pk>', UserDelete.as_view()),
    path('user/retrieve/<int:pk>', UserRetrieveUpdate.as_view()),

    path('book/create', BookRegistration.as_view()),
    path('book/update/<int:pk>', BookRetrieveUpdate.as_view()),
    path('book/list', BookList.as_view()),
    path('book/delete/<int:pk>', BookRetrieveUpdate.as_view()),
    path('book/retrieve/<int:pk>', BookRetrieveUpdate.as_view()),

    path('role/create', RoleRegistration.as_view()),
    path('role/update/<int:pk>', RoleRetrieveUpdate.as_view()),
    path('role/list', RoleList.as_view()),
    path('role/delete/<int:pk>', RoleRetrieveUpdate.as_view()),
    path('role/retrieve/<int:pk>', RoleRetrieveUpdate.as_view()),

    path('category/create', CategoryRegistration.as_view()),
    path('category/update/<int:pk>', CategoryRetrieveUpdate.as_view()),
    path('category/list', CategoryList.as_view()),
    path('category/delete/<int:pk>', CategoryRetrieveUpdate.as_view()),
    path('category/retrieve/<int:pk>', CategoryRetrieveUpdate.as_view()),

    path('book_category/create', BookCategoryRegistration.as_view()),
    path('book_category/update/<int:pk>', BookCategoryRetrieveUpdate.as_view()),
    path('book_category/list', BookCategoryList.as_view()),
    path('book_category/delete/<int:pk>', BookCategoryDelete.as_view()),
    path('book_category/retrieve/<int:pk>', BookCategoryRetrieveUpdate.as_view()),

    path('issue_book/create', IssueBookRegistration.as_view()),
    path('issue_book/update/<int:pk>', IssueBookRetrieveUpdate.as_view()),
    path('issue_book/list', IssueBookList.as_view()),
    path('issue_book/delete/<int:pk>', IssueBookRetrieveUpdate.as_view()),
    path('issue_book/retrieve/<int:pk>', IssueBookRetrieveUpdate.as_view()),
    path('issue_book/return/<int:pk>', ReturnBook.as_view()),

    path('reserve_book/create', ReserveBookRegistration.as_view()),
    path('reserve_book/update/<int:pk>', ReserveBookRetrieveUpdate.as_view()),
    path('reserve_book/list', ReserveBookList.as_view()),
    path('reserve_book/delete/<int:pk>', ReserveBookRetrieveUpdate.as_view()),
    path('reserve_book/retrieve/<int:pk>', ReserveBookRetrieveUpdate.as_view()),

    path('user_role/create', UserRoleRegistration.as_view()),
    path('user_role/update/<int:pk>', UserRoleRetrieveUpdate.as_view()),
    path('user_role/list', UserRoleList.as_view()),
    path('user_role/delete/<int:pk>', UserRoleDelete.as_view()),
    path('user_role/retrieve/<int:pk>', UserRoleRetrieveUpdate.as_view())
    ]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from rest_framework.permissions import BasePermission

from lmsapp.models import UserRole


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        authenticated_user_id = request.user.id
        urobj = UserRole.objects.get(pk=authenticated_user_id)
        user_role = urobj.role_name.name
        if user_role != 'Admin':
            if request.method == 'GET':
                return True
            else:
                return False
        return True
